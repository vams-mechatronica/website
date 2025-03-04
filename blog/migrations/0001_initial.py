# Generated by Django 5.1.6 on 2025-03-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('author', models.CharField(max_length=250, verbose_name='Author')),
                ('category', models.CharField(blank=True, max_length=50, null=True, verbose_name='Category')),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Blog Image')),
                ('date', models.DateField(verbose_name='Date Posted')),
                ('post_url', models.CharField(blank=True, max_length=500, null=True, verbose_name='Blog Url')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
