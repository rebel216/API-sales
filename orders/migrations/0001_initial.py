# Generated by Django 4.0.6 on 2022-07-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_slug', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=200)),
            ],
        ),
    ]
