# Generated by Django 3.2.19 on 2023-05-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_tweet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.CharField(default='86c58758cff744b08b3337c09b6ca3b5', editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
