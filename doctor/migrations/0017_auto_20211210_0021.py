# Generated by Django 3.2.7 on 2021-12-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0016_auto_20211210_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='day',
            field=models.CharField(choices=[('Saturday', 'Saturday'), ('Friday ', 'Friday '), ('Tuesday', 'Tuesday'), ('Monday', 'Monday'), ('Sunday', 'Sunday'), ('Thursday', 'Thursday'), ('Wednesday', 'Wednesday')], default='Saturday', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='end_time',
            field=models.TimeField(null=True),
        ),
    ]
