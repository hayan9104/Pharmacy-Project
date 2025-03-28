# Generated by Django 5.1.4 on 2025-03-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_site', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='badge',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='delay',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='reviews_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='delay',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon_class',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
