# Generated by Django 2.2.5 on 2021-03-21 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_room_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]