# Generated by Django 5.0 on 2023-12-18 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_category_options_alter_product_options_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
