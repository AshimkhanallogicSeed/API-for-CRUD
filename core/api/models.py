from django.db import models

# Create your models here.
class company_list(models.Model):
    compID = models.AutoField(primary_key=True)
    compName = models.CharField(max_length=255)
    compAddress = models.CharField(max_length=255)
    compCity = models.CharField(max_length=255)
    compState = models.CharField(max_length=255)
    compURL = models.URLField(max_length=255)
    compEstd = models.DateField()
    compType = models.CharField(max_length=255)
    compSize = models.CharField(max_length=255)
    compISIN = models.CharField(max_length=255)
    def __str__(self):
        return self.compName