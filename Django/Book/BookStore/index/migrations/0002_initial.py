# Generated by Django 3.0.7 on 2020-11-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=16, verbose_name='账号')),
                ('passwd', models.CharField(max_length=16, verbose_name='密码')),
            ],
        ),
    ]