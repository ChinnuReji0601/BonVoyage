# Generated by Django 5.1.4 on 2024-12-15 20:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0015_alter_tablepayment_expiry_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablepayment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
