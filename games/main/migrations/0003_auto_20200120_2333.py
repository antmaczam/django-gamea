# Generated by Django 2.2.7 on 2020-01-20 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200120_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='comments',
            field=models.PositiveIntegerField(),
        ),
    ]
