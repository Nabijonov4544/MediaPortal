# Generated by Django 4.2.1 on 2023-05-22 08:37

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BestStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=30, verbose_name='Familya')),
                ('group', models.CharField(max_length=10, verbose_name='guruh')),
                ('shortly_description', models.CharField(max_length=60, verbose_name='qisqacha izoh')),
                ('image', models.ImageField(upload_to='students/', verbose_name='rasm')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Izoh')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Iqtidorli Talaba',
                'verbose_name_plural': 'Iqtidorli Talabalar',
            },
        ),
        migrations.CreateModel(
            name='Tuiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=17, unique=True, verbose_name='Telefon raqami')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tuiters/', verbose_name='rasm')),
                ('bio', models.TextField(verbose_name='izoh')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tuiterlar',
            },
        ),
    ]