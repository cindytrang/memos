# Generated by Django 5.1.1 on 2024-10-01 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crush',
            fields=[
                ('crushId', models.AutoField(primary_key=True, serialize=False)),
                ('crushName', models.CharField(max_length=100)),
                ('mood', models.CharField(max_length=100)),
                ('matchingMoodEntries', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('diaryId', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SignInDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entryId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('mood', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('diaryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='diaryapp.diary')),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('lockerId', models.AutoField(primary_key=True, serialize=False)),
                ('diaryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diary', to='diaryapp.diary')),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('memoId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('locker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memos', to='diaryapp.locker')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('eyeColour', models.CharField(max_length=10)),
                ('hairColour', models.CharField(max_length=20)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diaryapp.signindetail')),
            ],
        ),
        migrations.AddField(
            model_name='diary',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diaryapp.user'),
        ),
    ]
