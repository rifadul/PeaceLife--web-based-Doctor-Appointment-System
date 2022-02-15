# Generated by Django 3.2.7 on 2021-12-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecelife', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='testimonial_images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
