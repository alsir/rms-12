from django.db import models

# Create your models here.
class risk(models.Model):
  risk_id =models.CharField(max_length=20)
  risk_name =models.CharField(max_length=50)
  risk_description =models.CharField(max_length=250)
  risk_level=models.CharField(max_length=20)
  department_name =models.CharField(max_length=50)
