# Generated by Django 5.1.2 on 2024-11-09 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0006_agent_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='avatars/')),
            ],
        ),
        migrations.RemoveField(
            model_name='agent',
            name='image_url',
        ),
        migrations.AddField(
            model_name='agent',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agents', to='agents.avatar'),
        ),
    ]
