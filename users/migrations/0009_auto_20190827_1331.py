# Generated by Django 2.2.4 on 2019-08-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190806_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default='https://'),
        ),
    ]
