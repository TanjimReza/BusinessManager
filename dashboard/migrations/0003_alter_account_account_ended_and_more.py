# Generated by Django 4.0.4 on 2022-05-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_account_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_ended',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_refil_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_started',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_ends',
            field=models.DateField(auto_now=True),
        ),
    ]
