# Generated by Django 2.2.5 on 2021-04-22 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]