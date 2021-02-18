# Generated by Django 3.1.4 on 2020-12-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0009_auto_20201212_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='popular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='shoe',
        ),
    ]
