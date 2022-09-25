# Generated by Django 3.2.15 on 2022-09-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_alter_review_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('info', models.TextField()),
                ('size', models.TextField()),
                ('cold', models.TextField()),
                ('cups', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]