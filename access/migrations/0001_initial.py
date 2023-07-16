# Generated by Django 4.2.3 on 2023-07-15 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSHKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='default', max_length=32)),
                ('pub_key', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ssh_keys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('GRANTED', 'GRANTED'), ('REMOVED', 'REMOVED'), ('FAILED', 'FAILED')], default='PENDING', max_length=15)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accesses', to='hosts.host')),
                ('ssh_key', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accesses', to='access.sshkeys')),
            ],
        ),
    ]
