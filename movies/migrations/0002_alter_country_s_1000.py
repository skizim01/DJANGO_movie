# Generated by Django 4.0.2 on 2022-05-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='s_1000',
            field=models.FloatField(verbose_name='Кількість солдат на тисячу населення'),
        ),
    ]
