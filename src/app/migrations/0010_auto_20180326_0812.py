# Generated by Django 2.0.3 on 2018-03-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180322_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='notify_to',
            field=models.TextField(default=''),
        ),
    ]