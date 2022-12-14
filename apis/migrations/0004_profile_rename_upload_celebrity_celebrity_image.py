# Generated by Django 4.0.5 on 2022-08-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_rename_celebrity_data_celebrity'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10)),
                ('user_image', models.ImageField(upload_to='uploads/')),
                ('user_about', models.CharField(max_length=100)),
                ('user_tag', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='celebrity',
            old_name='upload',
            new_name='celebrity_image',
        ),
    ]
