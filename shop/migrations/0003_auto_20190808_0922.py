# Generated by Django 2.2.2 on 2019-08-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190807_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('0', 'Art & Crafts'), ('1', 'Baby'), ('2', 'Beauty & Personal care'), ('3', 'Books'), ('4', 'Computers'), ('5', 'Electronics'), ('6', "Women's Fashion"), ('7', "Men's Fashion"), ('8', "Girl's Fashion"), ('9', "Boys's Fashion"), ('10', 'Home & Kitchen'), ('11', 'Others')], max_length=50),
        ),
    ]
