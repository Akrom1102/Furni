# Generated by Django 5.0.6 on 2024-06-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_category_code_product_subcategory_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_name',
            field=models.CharField(default=1, max_length=20, verbose_name='Kategoriya nomi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory_name',
            field=models.CharField(default=1, max_length=20, verbose_name='Ost-kategoriya-nomi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category_code',
            field=models.CharField(max_length=50, verbose_name='Kategoriya kodi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ost-kategoriya-kodi'),
        ),
        migrations.AlterField(
            model_name='users',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Name'),
        ),
    ]