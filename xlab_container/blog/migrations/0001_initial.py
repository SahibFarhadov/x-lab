# Generated by Django 4.2.8 on 2024-01-26 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kateqoriya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kateqoriya_adi', models.CharField(max_length=150, verbose_name='Kateqoriya adı')),
                ('kateqoriya_slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Kateqoriya',
                'verbose_name_plural': 'Kateqoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basliq_sekli', models.ImageField(blank=True, default='uploads/default.jpg', null=True, upload_to='uploads/%d.%m.%Y')),
                ('basliq', models.CharField(max_length=200, verbose_name='Məqalə başlığı')),
                ('kontent', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Məqalə kontenti')),
                ('yaradilma_tarixi', models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi')),
                ('deyisdirilme_tarixi', models.DateTimeField(auto_now=True, verbose_name='Yaranma tarixi')),
                ('blog_slug', models.SlugField(editable=False, unique=True)),
                ('yayinda_mi', models.BooleanField(default=False, verbose_name='Yayına buraxılsın?')),
                ('yeni_mi', models.BooleanField(default=True, verbose_name='Yeni məqalə?')),
                ('karuselde', models.BooleanField(default=False, verbose_name='Karuseldə')),
                ('blog_kateqoriya', models.ManyToManyField(to='blog.kateqoriya', verbose_name='Kateqoriyaları seçin.')),
                ('istifadeci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='İstifadəçi')),
            ],
            options={
                'verbose_name': 'Məqalə',
                'verbose_name_plural': 'Məqalələr',
            },
        ),
    ]
