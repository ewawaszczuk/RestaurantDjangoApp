# Generated by Django 3.0 on 2020-02-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrescoBasilico', '0006_auto_20200201_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
