# Generated by Django 4.0.2 on 2022-02-19 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_lug_product_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount_rate',
            new_name='discountRate',
        ),
    ]