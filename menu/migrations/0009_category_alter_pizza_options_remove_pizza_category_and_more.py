# Generated by Django 4.2 on 2023-05-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_pizza_options_alter_pizza_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Fruity', 'Fruity'), ('Vegan', 'Vegan'), ('Popular', 'Popular')], max_length=10, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='pizza',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='category',
        ),
        migrations.AddField(
            model_name='pizza',
            name='categories',
            field=models.ManyToManyField(to='menu.category'),
        ),
    ]
