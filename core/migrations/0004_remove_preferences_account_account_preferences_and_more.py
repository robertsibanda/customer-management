# Generated by Django 5.0.4 on 2024-04-22 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_account_personal_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='account',
        ),
        migrations.AddField(
            model_name='account',
            name='preferences',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.preferences'),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]
