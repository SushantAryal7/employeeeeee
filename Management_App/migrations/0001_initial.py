# Generated by Django 4.0.4 on 2022-05-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('employee_id', models.PositiveIntegerField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('time', models.PositiveIntegerField(max_length=30)),
            ],
        ),
    ]
