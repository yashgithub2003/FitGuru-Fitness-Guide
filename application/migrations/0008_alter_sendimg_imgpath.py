# Generated by Django 5.1.7 on 2025-04-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_sendimg_delete_custplan_delete_imageselection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendimg',
            name='imgpath',
            field=models.JSONField(),
        ),
    ]
