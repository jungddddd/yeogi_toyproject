# Generated by Django 4.2.13 on 2024-06-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_alter_todoitem_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='description',
            new_name='content',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='todos/'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
