# Generated by Django 2.2.1 on 2020-10-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_goods_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_type',
            name='logo',
            field=models.ImageField(upload_to='img'),
        ),
    ]
