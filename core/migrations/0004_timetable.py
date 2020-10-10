# Generated by Django 3.1.2 on 2020-10-09 08:00

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201008_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('weekdays', multiselectfield.db.fields.MultiSelectField(choices=[('saturday', 'Saturday'), ('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday')], max_length=56)),
                ('start_time', models.TimeField(auto_now_add=True)),
                ('end_time', models.TimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]