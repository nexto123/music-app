# Generated by Django 2.2.4 on 2019-09-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0005_auto_20190922_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmusic',
            name='genre',
            field=models.CharField(default='world music', max_length=30),
        ),
    ]