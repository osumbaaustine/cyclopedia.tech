# Generated by Django 3.2.23 on 2023-12-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_entry_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(default='No Title', max_length=200),
        ),
    ]
