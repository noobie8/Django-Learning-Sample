# Generated by Django 5.0.7 on 2024-07-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='poster',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='year',
            field=models.IntegerField(),
        ),
    ]
