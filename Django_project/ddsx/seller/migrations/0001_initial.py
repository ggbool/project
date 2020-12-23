# Generated by Django 2.2.1 on 2020-10-13 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=32)),
                ('gender', models.BooleanField(default=True)),
                ('address', models.TextField()),
                ('head_img', models.ImageField(null=True, upload_to='img')),
            ],
        ),
    ]