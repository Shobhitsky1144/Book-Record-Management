# Generated by Django 3.0.6 on 2020-07-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BRMapp', '0003_auto_20200730_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brmuser',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
    ]