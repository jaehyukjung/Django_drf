# Generated by Django 3.2.15 on 2022-10-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20221002_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
