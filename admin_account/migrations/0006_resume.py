# Generated by Django 4.2.3 on 2023-09-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_account', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
    ]