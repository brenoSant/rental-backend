# Generated by Django 4.1.3 on 2022-11-16 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(db_column='id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(db_column='id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='id',
            field=models.BigAutoField(db_column='id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(db_column='id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rental',
            name='id',
            field=models.BigAutoField(db_column='id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rentalitem',
            name='id',
            field=models.BigAutoField(db_column='id', primary_key=True, serialize=False),
        ),
    ]
