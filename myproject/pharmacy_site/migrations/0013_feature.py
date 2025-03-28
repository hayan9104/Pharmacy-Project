# Generated by Django 5.1.4 on 2025-03-23 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_site', '0012_hero_alter_menulink_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(help_text='Font Awesome icon class (e.g., fas fa-pills)', max_length=50)),
                ('title', models.CharField(help_text='Feature title', max_length=100)),
                ('description', models.TextField(help_text='Feature description')),
                ('order', models.IntegerField(default=0, help_text='Order of appearance')),
                ('is_active', models.BooleanField(default=True, help_text='Whether to display this feature')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
                'ordering': ['order'],
            },
        ),
    ]
