# Generated by Django 3.2.7 on 2021-12-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_alter_doctorschedule_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Saturday', 'Saturday'), ('Tuesday', 'Tuesday'), ('Thursday', 'Thursday'), ('Wednesday', 'Wednesday'), ('Friday ', 'Friday '), ('Monday', 'Monday')], default='Saturday', max_length=100),
        ),
    ]
