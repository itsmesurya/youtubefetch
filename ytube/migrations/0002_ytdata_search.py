# Generated by Django 2.0.3 on 2019-05-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ytube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ytdata',
            name='search',
            field=models.CharField(default='null', max_length=10),
        ),
    ]
