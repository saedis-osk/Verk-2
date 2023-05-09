# Generated by Django 4.2 on 2023-05-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_user_account_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='profiles'),
        ),
    ]
