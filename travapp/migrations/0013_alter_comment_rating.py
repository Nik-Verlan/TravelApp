# Generated by Django 3.2 on 2021-04-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travapp', '0012_alter_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=5, null=True, verbose_name='Оценка'),
        ),
    ]