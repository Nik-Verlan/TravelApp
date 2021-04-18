# Generated by Django 3.2 on 2021-04-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travapp', '0009_remove_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='comment',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='country',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=5, null=True, verbose_name='Оценка'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]