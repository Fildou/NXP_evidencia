# Generated by Django 4.0.3 on 2022-06-02 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_item_free_count_remove_item_full_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='borrowed_item',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.item'),
        ),
    ]