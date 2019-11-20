# Generated by Django 2.2.7 on 2019-11-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=1000)),
                ('task_img', models.ImageField(default='NULL', upload_to='task_img/')),
                ('task_text', models.TextField(default='')),
                ('task_code', models.TextField(default='')),
                ('isSolved', models.BooleanField(default=False)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
