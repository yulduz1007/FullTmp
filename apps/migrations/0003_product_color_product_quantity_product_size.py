# Generated by Django 5.1.2 on 2024-10-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_category_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
