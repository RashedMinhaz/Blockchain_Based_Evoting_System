# Generated by Django 4.0.2 on 2022-03-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters',
            name='uuid',
            field=models.IntegerField(max_length=20, primary_key=True, serialize=False),
        ),
    ]