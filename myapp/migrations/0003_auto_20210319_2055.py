# Generated by Django 2.2.5 on 2021-03-19 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210225_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=20)),
                ('end', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameroom', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('userID', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bike',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User'),
        ),
    ]