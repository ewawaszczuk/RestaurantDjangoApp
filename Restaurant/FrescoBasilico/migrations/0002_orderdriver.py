# Generated by Django 3.0 on 2020-01-25 09:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FrescoBasilico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order_picked_up_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
