# Generated by Django 5.0.4 on 2024-05-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_exemption'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertySale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=14)),
                ('township_code', models.IntegerField(blank=True, null=True)),
                ('neighborhood_code', models.IntegerField(blank=True, null=True)),
                ('class_code', models.CharField(blank=True, max_length=500, null=True)),
                ('is_mydec_date', models.CharField(blank=True, max_length=500, null=True)),
                ('sale_document_num', models.FloatField(blank=True, null=True)),
                ('num_parcels_sale', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('sale_date', models.DateField(blank=True, null=True)),
                ('sale_price', models.BigIntegerField(blank=True, null=True)),
                ('sale_deed_type', models.CharField(blank=True, max_length=500, null=True)),
                ('mydec_deed_type', models.CharField(blank=True, max_length=500, null=True)),
                ('sale_seller_name', models.CharField(blank=True, max_length=500, null=True)),
                ('sale_buyer_name', models.CharField(blank=True, max_length=500, null=True)),
                ('pin_id', models.IntegerField(blank=True, null=True)),
                ('sale_type', models.CharField(blank=True, max_length=500, null=True)),
                ('sale_filter_same_sale_within_365', models.CharField(blank=True, max_length=500, null=True)),
                ('sale_filter_less_than_10k', models.CharField(blank=True, max_length=500, null=True)),
                ('sale_filter_deed_type', models.CharField(blank=True, max_length=500, null=True)),
                ('is_multisale', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'property_sale',
            },
        ),
    ]
