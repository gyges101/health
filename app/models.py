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


class Rdv(models.Model):

    nom = models.CharField(max_length=9000)
    email = models.EmailField(blank=True, null=True)
    tele = models.CharField(max_length=900)
    date = models.CharField(max_length=9000)
    heure = models.CharField(max_length=9000)
    genre = models.CharField(max_length=600)
    service = models.CharField(max_length=9000)
    age = models.CharField(max_length=800)

    def __str__(self):
        return str(self.nom) + " | - | " + str(self.pk)

class Blog(models.Model):

    image = models.ImageField(upload_to='blog_image', default='blog_image/healt.jpg')
    date = models.DateField(auto_now=True)
    titre = models.CharField(max_length=1000)
    paragraphe = models.CharField(max_length=9999)

    def __str__(self):
        return str(self.titre)