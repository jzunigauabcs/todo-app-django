# Generated by Django 4.2.7 on 2023-11-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='Created At')),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
