# Generated by Django 3.2.6 on 2022-05-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manejadorUsuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
