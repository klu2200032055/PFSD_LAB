# Generated by Django 5.0 on 2024-02-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_alter_register_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=216)),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
    ]