# Generated by Django 5.1.4 on 2025-03-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_site', '0009_menuitem_menusection_menulink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='parent',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
