# Generated by Django 4.2.3 on 2023-07-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=20)),
                ('duration_minutes', models.IntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
