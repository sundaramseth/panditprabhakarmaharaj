# Generated by Django 4.2.4 on 2023-08-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
