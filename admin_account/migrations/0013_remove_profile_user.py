# Generated by Django 4.2.3 on 2023-09-02 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_account', '0012_profile_delete_projectrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]