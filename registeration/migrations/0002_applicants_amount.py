# Generated by Django 4.1.1 on 2022-10-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='amount',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
