# Generated by Django 3.2 on 2021-04-16 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travapp', '0010_auto_20210414_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='country',
            name='rating',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Короткий коммент')),
                ('comment', models.TextField(null=True, verbose_name='Опишите ваш отдых')),
                ('rating', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=5, null=True, verbose_name='Оценка')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travapp.country')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
