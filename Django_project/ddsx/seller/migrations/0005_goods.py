# Generated by Django 2.2.1 on 2020-10-14 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_auto_20201013_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('shelf_life', models.IntegerField()),
                ('product_dt', models.DateField(null=True)),
                ('desc', models.TextField()),
                ('logo', models.ImageField(upload_to='img')),
                ('content', models.TextField()),
                ('goodstype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Goods_Type')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.Store')),
            ],
        ),
    ]
