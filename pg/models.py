from django.db import models

# Create your models here.
class Pass_gen(models.Model):
    Full_name = models.CharField(max_length=250)
    Email_ID = models.EmailField(max_length=250)