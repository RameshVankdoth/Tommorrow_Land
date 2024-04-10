# Generated by Django 4.1.4 on 2022-12-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_electronics_pro_image2_electronics_pro_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronics',
            name='pro_desc',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='gaming',
            name='game_desc',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_description',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='veh_desc',
            field=models.TextField(max_length=1500),
        ),
    ]