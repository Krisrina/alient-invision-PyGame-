# Generated by Django 3.0.2 on 2020-02-29 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_entry_verified_adm'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tag',
            field=models.CharField(default='', max_length=100),
        ),
    ]
