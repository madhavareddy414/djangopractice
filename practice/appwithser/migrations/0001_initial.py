# Generated by Django 3.1.4 on 2021-04-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=250)),
                ('esal', models.FloatField()),
                ('edd', models.CharField(max_length=250)),
            ],
        ),
    ]
