from rest_framework.views import APIView
from django.db import transaction

# Create your views here.
import csv
from concurrent.futures import ThreadPoolExecutor
from .models import TestModel
from rest_framework.response import Response


class TestImport(APIView):
    def post(self, request, *args, **kwargs):
        def import_csv(file):

            data_source = file.read().decode("utf-8-sig")

            def stream_data():
                reader = csv.reader(data_source.splitlines())
                columns = next(reader)
                chunk_size = 1000
                end_of_file = False

                while not end_of_file:
                    chunk = []
                    for _ in range(chunk_size):
                        try:
                            row = next(reader)

                        except StopIteration:

                            end_of_file = True
                            break
                        row_dict = {
                            columns[i]: row[i]
                            for i in range(min(len(columns), len(row)))
                        }

                        model_instance = TestModel(**row_dict)

                        chunk.append(model_instance)
                    if chunk:
                        yield chunk

            save_data(stream_data())

        files = request.data.getlist("files")
        with ThreadPoolExecutor() as executor:
            futures = []
            for csv_file in files:
                futures.append(executor.submit(import_csv, csv_file))

            # Wait for all tasks to complete
            for future in futures:
                future.result()

        return Response("Data import completed successfully.")


def save_data(generator):
    with transaction.atomic():

        for chunk in generator:
            TestModel.objects.bulk_create(chunk)
