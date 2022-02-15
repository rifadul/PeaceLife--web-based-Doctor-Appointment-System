# Generated by Django 3.2.7 on 2021-12-03 14:07

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='medical/department/')),
                ('about', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('designation', models.CharField(max_length=100)),
                ('about', ckeditor.fields.RichTextField()),
                ('education', ckeditor.fields.RichTextField()),
                ('experience', ckeditor.fields.RichTextField()),
                ('consulting_fee', models.FloatField(null=True)),
                ('image', models.ImageField(upload_to='Doctor/images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.department')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Saturday', 'Saturday'), ('Thursday', 'Thursday'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Friday ', 'Friday ')], default='Saturday', max_length=100)),
                ('start_time', models.CharField(max_length=50, null=True)),
                ('end_time', models.CharField(max_length=50, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
