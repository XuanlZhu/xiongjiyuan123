# Generated by Django 3.2.7 on 2021-10-19 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='path',
            field=models.CharField(max_length=64),
        ),
    ]
