# Generated by Django 3.2 on 2021-05-01 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
    ]