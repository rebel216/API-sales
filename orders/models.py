from django.db import models

# Create your models here.
class Data(models.Model):
    user_slug = models.CharField(max_length=200)
    file = models.FileField(upload_to='API/')
 