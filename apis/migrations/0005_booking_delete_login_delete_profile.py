# Generated by Django 4.0.5 on 2022-08-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_profile_rename_upload_celebrity_celebrity_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Occasion', models.CharField(max_length=20)),
                ('Video_date', models.DateField()),
                ('To', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
