# Generated by Django 4.1.4 on 2022-12-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronics',
            name='pro_image1',
            field=models.ImageField(default='default', upload_to=''),
        ),
    ]