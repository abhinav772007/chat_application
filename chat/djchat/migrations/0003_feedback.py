# Generated by Django 5.1.6 on 2025-02-23 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djchat', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rattings', models.CharField(max_length=1000)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
    ]
