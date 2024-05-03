from django.db import models

# Create your models here.
class TestModel(models.Model):
    title=models.CharField(max_length=100)
    
    
class Exemption(models.Model):

    PIN=models.CharField(max_length=14,db_index=True)
    Tax_Year = models.IntegerField(null=True, blank=True,db_index=True)
    Stat1 = models.IntegerField(null=True, blank=True)
    Stat2 = models.IntegerField(null=True, blank=True)
    Tri_Loc = models.TextField(null=True, blank=True)
    Exe_Type = models.TextField(null=True, blank=True)
    HO_Ex_EAV = models.IntegerField(null=True, blank=True)
    HS_Ex_EAV = models.IntegerField(null=True, blank=True)
    SF_Ex_EAV = models.IntegerField(null=True, blank=True)

    LT_Ex_EAV = models.IntegerField(null=True, blank=True)
    DisPer_EAV = models.IntegerField(null=True, blank=True)

    RetVet_EAV = models.IntegerField(null=True, blank=True)
    DisVet_EAV = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "exemption"
        unique_together=['PIN',"Tax_Year"]

    def __str__(self) -> str:
        return str(self.Tax_Year)
    
class PropertySale(models.Model):

    pin=models.CharField(max_length=14)
    township_code = models.IntegerField(null=True, blank=True)
    neighborhood_code = models.IntegerField(null=True, blank=True)
    class_code = models.CharField(null=True, blank=True, max_length=500)
    is_mydec_date = models.CharField(max_length=500, null=True, blank=True)
    sale_document_num = models.FloatField(null=True, blank=True)
    num_parcels_sale = models.CharField(null=True, blank=True, max_length=200)
    year = models.IntegerField(null=True, blank=True)
    sale_date = models.DateField(null=True, blank=True)
    sale_price = models.BigIntegerField(null=True, blank=True)
    sale_deed_type = models.CharField(max_length=500, null=True, blank=True)
    mydec_deed_type = models.CharField(max_length=500, null=True, blank=True)
    sale_seller_name = models.CharField(max_length=500, blank=True, null=True)
    sale_buyer_name = models.CharField(max_length=500, blank=True, null=True)
    pin_id = models.IntegerField(blank=True, null=True)
    sale_type = models.CharField(max_length=500, null=True, blank=True)
    sale_filter_same_sale_within_365 = models.CharField(
        max_length=500, null=True, blank=True
    )
    sale_filter_less_than_10k = models.CharField(max_length=500, null=True, blank=True)
    sale_filter_deed_type = models.CharField(max_length=500, null=True, blank=True)
    is_multisale = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = "property_sale"