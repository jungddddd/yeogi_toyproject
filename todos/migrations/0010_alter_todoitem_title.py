# Generated by Django 5.0.6 on 2024-06-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_remove_todoitem_due_date_remove_todoitem_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
