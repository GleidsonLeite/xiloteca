# Generated by Django 2.1.1 on 2019-03-17 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wood', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='madeira',
            name='observacoes',
        ),
    ]