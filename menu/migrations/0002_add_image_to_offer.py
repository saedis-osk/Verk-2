from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='image',
            field=models.ImageField(default='offer/default.png', upload_to='offer/'),
        ),
    ]
