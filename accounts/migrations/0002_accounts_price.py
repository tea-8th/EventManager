# Generated by Django 3.2.9 on 2021-11-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
