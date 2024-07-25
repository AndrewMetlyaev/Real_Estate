# Generated by Django 5.0.6 on 2024-07-25 14:33

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
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bedrooms', models.PositiveIntegerField()),
                ('property_type', models.CharField(choices=[('APARTMENT', 'APARTMENT'), ('HOUSE', 'HOUSE'), ('VILLA', 'VILLA'), ('HOSTEL', 'HOSTEL'), ('CAMPING', 'CAMPING')], max_length=20)),
                ('available', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
