# Generated by Django 3.2.15 on 2022-10-20 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_coffee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_number', models.IntegerField()),
                ('point', models.IntegerField(null=True)),
            ],
        ),
    ]
