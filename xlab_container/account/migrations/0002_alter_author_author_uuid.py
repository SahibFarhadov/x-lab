# Generated by Django 4.2.8 on 2024-01-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_uuid',
            field=models.UUIDField(editable=False, null=True),
        ),
    ]
