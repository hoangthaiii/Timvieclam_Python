# Generated by Django 3.1.5 on 2021-04-03 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCatalog', models.CharField(max_length=50, verbose_name='Loại công việc')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameJob', models.CharField(max_length=100, verbose_name='Tên công việc')),
                ('motacv', models.TextField(verbose_name='Mô Tả công việc')),
                ('phucloi', models.TextField(verbose_name='Phúc lợi')),
                ('yeucaucv', models.TextField(verbose_name='Yêu cầu conog việc')),
                ('salary', models.CharField(max_length=50, verbose_name='Lương')),
                ('diachi', models.CharField(max_length=50, verbose_name='Địa chỉ')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Hình ảnh')),
                ('catalogy', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Home.catalogy')),
                ('nhatuyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Họ và tên')),
                ('email', models.CharField(max_length=100, verbose_name='Địa chỉ email')),
                ('cv_file', models.FileField(blank=True, null=True, upload_to='CV_File/', verbose_name='Chọn CV File')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]