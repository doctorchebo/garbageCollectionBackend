# Generated by Django 4.1.4 on 2022-12-08 23:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=20, max_digits=50, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=20, max_digits=50, null=True)),
                ('cleaning_state', models.CharField(blank=True, choices=[('NC', 'Not Cleaned'), ('CL', 'Cleaning'), ('CD', 'Cleaned')], max_length=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
