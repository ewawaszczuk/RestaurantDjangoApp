# Generated by Django 3.0 on 2020-02-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrescoBasilico', '0004_auto_20200125_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='image',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]