# Generated by Django 3.2.6 on 2021-11-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_rename_myclubuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='manager',
            field=models.CharField(default='SOME STRING', max_length=60),
        ),
    ]