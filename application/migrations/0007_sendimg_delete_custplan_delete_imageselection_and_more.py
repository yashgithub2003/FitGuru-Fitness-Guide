# Generated by Django 5.1.7 on 2025-04-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_imageselection'),
    ]

    operations = [
        migrations.CreateModel(
            name='sendimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('imgpath', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='custplan',
        ),
        migrations.DeleteModel(
            name='ImageSelection',
        ),
        migrations.DeleteModel(
            name='plancust',
        ),
    ]
