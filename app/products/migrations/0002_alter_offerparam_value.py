# Generated by Django 3.2.2 on 2022-07-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerparam',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
