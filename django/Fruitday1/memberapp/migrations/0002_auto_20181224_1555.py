# Generated by Django 2.1.4 on 2018-12-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='unit',
            field=models.CharField(default='500g', max_length=20, verbose_name='单位'),
        ),
    ]
