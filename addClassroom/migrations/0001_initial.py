# Generated by Django 3.2.4 on 2021-06-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='教室名稱')),
                ('place', models.CharField(max_length=40, verbose_name='教室位置')),
                ('description', models.TextField(verbose_name='教室描述')),
                ('logInTime', models.DateTimeField(auto_now_add=True, verbose_name='新增時間')),
            ],
        ),
    ]
