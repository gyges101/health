# Generated by Django 2.2 on 2021-07-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rdv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=9000)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tele', models.CharField(max_length=900)),
                ('date', models.CharField(max_length=9000)),
                ('heure', models.CharField(max_length=9000)),
                ('genre', models.CharField(max_length=600)),
                ('service', models.CharField(max_length=9000)),
                ('age', models.CharField(max_length=800)),
            ],
        ),
    ]
