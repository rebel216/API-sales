from django.db import models

# Create your models here.
class Data(models.Model):
    user_slug = models.CharField(max_length=200)
    filename = models.FileField(upload_to='uploads')
