# Generated by Django 5.0.3 on 2024-04-23 19:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='reqeusted_money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('GBP', 'GB Pounds'), ('USD', 'US Dollars'), ('EUR', 'Euros')], default='GBP', max_length=3)),
                ('amount', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success'), ('Cancelled', 'Cancelled')], max_length=200)),
                ('From', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
