# Generated by Django 2.2.7 on 2019-12-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='isHelped',
            field=models.BooleanField(default=False),
        ),
    ]
