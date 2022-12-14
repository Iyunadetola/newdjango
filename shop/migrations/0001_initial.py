# Generated by Django 4.1.1 on 2022-10-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
