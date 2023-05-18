# Generated by Django 3.2 on 2023-05-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20230514_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='row',
            field=models.PositiveIntegerField(default=0, verbose_name='Row'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='seat',
            field=models.PositiveIntegerField(default=0, verbose_name='Seat'),
            preserve_default=False,
        ),
    ]
