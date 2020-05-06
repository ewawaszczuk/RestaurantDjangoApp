# Generated by Django 3.0 on 2020-02-07 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FrescoBasilico', '0009_auto_20200207_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Driver',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivered_to_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_items',
        ),
        migrations.RemoveField(
            model_name='orderedmeals',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderedmeals',
            name='ordered_meals_order',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDriver',
        ),
        migrations.DeleteModel(
            name='OrderedMeals',
        ),
    ]
