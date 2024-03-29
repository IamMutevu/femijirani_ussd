# Generated by Django 2.0.5 on 2018-11-18 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(max_length=10)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('ID', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AgentCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Agent')),
            ],
        ),
    ]
