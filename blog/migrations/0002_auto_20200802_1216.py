# Generated by Django 3.0.8 on 2020-08-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(max_length=5000),
        ),
    ]
