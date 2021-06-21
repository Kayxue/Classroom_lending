# Generated by Django 3.2.4 on 2021-06-19 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addClassroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowDate', models.DateField(verbose_name='借出日期')),
                ('startTime', models.IntegerField(choices=[(0, '第一節'), (1, '第二節'), (2, '第三節'), (3, '第四節'), (4, '第五節'), (5, '第六節'), (6, '第七節'), (7, '第八節')], verbose_name='開始時間')),
                ('end', models.IntegerField(choices=[(0, '第一節'), (1, '第二節'), (2, '第三節'), (3, '第四節'), (4, '第五節'), (5, '第六節'), (6, '第七節'), (7, '第八節')], verbose_name='結束時間')),
                ('everyWeek', models.BooleanField(verbose_name='固定每週借用')),
                ('endDate', models.DateField(verbose_name='結束日期')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addClassroom.classroom', verbose_name='教室')),
            ],
        ),
    ]
