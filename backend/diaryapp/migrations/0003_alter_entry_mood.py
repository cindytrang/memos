# Generated by Django 5.1.1 on 2024-10-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0002_crush_characters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mood',
            field=models.CharField(choices=[('Musical', 'Musical'), ('Sporty', 'Sporty'), ('Artistic', 'Artistic'), ('Fashion', 'Fashion'), ('Nerdy', 'Nerdy')], max_length=100),
        ),
    ]
