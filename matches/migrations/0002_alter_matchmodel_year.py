# Generated by Django 5.0.1 on 2024-01-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchmodel',
            name='year',
            field=models.CharField(max_length=200),
        ),
    ]
