# Generated by Django 5.0.7 on 2024-08-04 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0009_rename_product_productvariant_product_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariant',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AlterUniqueTogether(
            name='productvariant',
            unique_together={('product', 'size', 'color')},
        ),
    ]
