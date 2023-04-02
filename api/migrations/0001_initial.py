# Generated by Django 4.1.7 on 2023-04-02 13:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('code_endpoint', models.CharField(max_length=255)),
                ('token_endpoint', models.CharField(max_length=255)),
                ('resource_endpoint', models.CharField(max_length=255)),
                ('client_id', models.CharField(max_length=255)),
                ('client_secret', models.CharField(max_length=255)),
                ('public_key', models.CharField(max_length=255)),
                ('scopes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('redirect_uris', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('disabled', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'provider',
            },
        ),
        migrations.AddIndex(
            model_name='provider',
            index=models.Index(fields=['name'], name='provider_name_816b21_idx'),
        ),
        migrations.AddIndex(
            model_name='provider',
            index=models.Index(fields=['client_id'], name='provider_client__2c8a28_idx'),
        ),
        migrations.AddIndex(
            model_name='provider',
            index=models.Index(fields=['disabled'], name='provider_disable_7e6278_idx'),
        ),
        migrations.AddConstraint(
            model_name='provider',
            constraint=models.UniqueConstraint(fields=('client_id',), name='provider_client_id_unique_index'),
        ),
    ]