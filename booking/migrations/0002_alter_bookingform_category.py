# Generated by Django 4.2.4 on 2023-11-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingform',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
