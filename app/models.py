from django.db import models

# Create your models here.


class Property(models.Model):

    title = models.CharField(max_length=9000)
    desc = models.CharField(max_length=9000)
    keys = models.CharField(max_length=9000)

    def __str__(self):
        return self.title

class Image(models.Model):

    alter = models.CharField(max_length=9000, default='Image')
    img = models.FileField(upload_to='galerie')

    def __str__(self):
        return str(self.alter)