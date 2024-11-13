# Generated by Django 5.1.2 on 2024-11-12 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0007_avatar_remove_agent_image_url_agent_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='available_roles',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='agent',
            name='available_skills',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='template',
            name='data',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
