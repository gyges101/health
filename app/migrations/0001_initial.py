# Generated by Django 2.2 on 2021-07-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alter', models.CharField(default='Image', max_length=9000)),
                ('img', models.FileField(upload_to='galerie')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=9000)),
                ('desc', models.CharField(max_length=9000)),
                ('keys', models.CharField(max_length=9000)),
            ],
        ),
    ]
