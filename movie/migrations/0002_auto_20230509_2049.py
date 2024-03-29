# Generated by Django 3.2 on 2023-05-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='middle_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='director',
            name='middle_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Middle Name'),
        ),
    ]
