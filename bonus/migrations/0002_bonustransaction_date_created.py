# Generated by Django 2.2.6 on 2019-11-14 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonustransaction',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]