# Generated by Django 3.1.4 on 2021-01-22 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ece', '0003_auto_20210121_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('fdep', models.CharField(max_length=30)),
                ('fsal', models.CharField(max_length=30)),
            ],
        ),
    ]
