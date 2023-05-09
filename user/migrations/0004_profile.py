# Generated by Django 4.2 on 2023-05-08 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.CharField(max_length=9999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.account')),
            ],
        ),
    ]
