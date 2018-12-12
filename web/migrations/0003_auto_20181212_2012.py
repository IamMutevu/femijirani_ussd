# Generated by Django 2.0.5 on 2018-12-12 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_auto_20181118_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentcredential',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='agent_id',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='lastName',
        ),
        migrations.AddField(
            model_name='agent',
            name='agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AgentCredential',
        ),
    ]
