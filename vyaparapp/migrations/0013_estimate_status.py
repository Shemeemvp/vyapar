# Generated by Django 4.2.3 on 2023-11-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0012_estimate_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
