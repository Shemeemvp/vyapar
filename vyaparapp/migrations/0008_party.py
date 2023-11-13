# Generated by Django 3.2.21 on 2023-11-04 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vyaparapp', '0007_auto_20231031_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=100)),
                ('gst_no', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('gst_type', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('openingbalance', models.CharField(blank=True, default='0', max_length=100, null=True)),
                ('payment', models.CharField(blank=True, max_length=100, null=True)),
                ('creditlimit', models.CharField(blank=True, default='0', max_length=100, null=True)),
                ('current_date', models.DateField(blank=True, max_length=255, null=True)),
                ('End_date', models.CharField(blank=True, max_length=255, null=True)),
                ('additionalfield1', models.CharField(blank=True, max_length=100, null=True)),
                ('additionalfield2', models.CharField(blank=True, max_length=100, null=True)),
                ('additionalfield3', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.company')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
