# Generated by Django 4.2.4 on 2023-10-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_typesofpuja_puja_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typesofpuja',
            name='puja_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
