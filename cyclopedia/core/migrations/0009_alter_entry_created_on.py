# Generated by Django 3.2.23 on 2023-12-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_entry_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
