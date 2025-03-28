# Generated by Django 5.1.4 on 2025-03-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy_site', '0003_alter_product_badge_alter_product_delay_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Main heading of the hero section', max_length=255)),
                ('subtitle', models.TextField(help_text='Short description below the title')),
                ('background_image', models.ImageField(help_text='Background image for the hero section', upload_to='hero_images/')),
                ('button_text', models.CharField(default='Shop Medicines', max_length=50)),
                ('button_link', models.URLField(default='#', help_text='Link for the call-to-action button')),
            ],
        ),
    ]
