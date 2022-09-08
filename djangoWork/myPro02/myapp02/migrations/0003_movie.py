# Generated by Django 4.0.6 on 2022-08-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp02', '0002_forecast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('point', models.TextField()),
                ('content', models.CharField(max_length=500)),
            ],
        ),
    ]
