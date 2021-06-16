# Generated by Django 3.2.4 on 2021-06-16 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('addClassroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='logInTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='新增時間'),
            preserve_default=False,
        ),
    ]
