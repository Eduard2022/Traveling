# Generated by Django 3.2 on 2022-01-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop2', '0011_auto_20220114_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='grop',
            field=models.CharField(choices=[('post', 'post'), ('about1', 'about1'), ('about2', 'about2'), ('about3', 'about3'), ('about', 'about')], default='post', max_length=20),
        ),
    ]
