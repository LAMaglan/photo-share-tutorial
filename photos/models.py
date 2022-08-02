from django.db import models

# Create your models here.
class Photo(models.Model):
    # one field called "file"
    file = models.FileField(upload_to="file")

