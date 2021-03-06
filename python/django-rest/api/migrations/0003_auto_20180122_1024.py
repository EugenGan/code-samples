# Generated by Django 2.0.1 on 2018-01-22 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_deviceproducer'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='deviceproducer',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DeviceProducer'),
        ),
    ]
