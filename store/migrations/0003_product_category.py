# Generated by Django 4.2.16 on 2024-09-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_color_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='Buttons', max_length=100),
            preserve_default=False,
        ),
    ]
