# Generated by Django 3.2.23 on 2023-12-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_entry_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
    ]