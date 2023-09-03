# Generated by Django 4.2.3 on 2023-09-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_account', '0004_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='photos/projects')),
                ('technologies', models.CharField(max_length=100)),
                ('project_url', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
