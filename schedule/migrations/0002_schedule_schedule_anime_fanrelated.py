# Generated by Django 2.1.7 on 2019-03-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='schedule_anime_fanrelated',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
