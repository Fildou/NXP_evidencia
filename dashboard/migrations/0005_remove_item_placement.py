# Generated by Django 4.0.3 on 2022-06-02 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_item_item_count_alter_borrowed_item_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='placement',
        ),
    ]