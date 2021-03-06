# Generated by Django 3.2 on 2022-01-14 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop2', '0007_auto_20220111_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='grop',
            field=models.CharField(choices=[('shoes', 'shoes'), ('post', 'post'), ('jeans', 'jeans'), ('shirts', 'shirts')], default='post', max_length=20),
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=255)),
                ('bodys', models.TextField()),
                ('header_images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post_dates', models.DateField(auto_now_add=True)),
                ('grops', models.CharField(choices=[('post', 'postt'), ('jeanss', 'jeanss')], default='jeanss', max_length=20)),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
