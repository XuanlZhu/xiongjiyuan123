# Generated by Django 3.0.7 on 2020-12-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_test_user_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_user',
            name='user',
            field=models.CharField(blank=True, max_length=16, unique=True, verbose_name='账号'),
        ),
    ]
