# Generated by Django 3.1.2 on 2020-10-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201010_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
