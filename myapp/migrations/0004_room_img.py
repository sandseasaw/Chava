# Generated by Django 2.2.5 on 2021-03-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210319_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='img',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]