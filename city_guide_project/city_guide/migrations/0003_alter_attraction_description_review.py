# Generated by Django 5.0.7 on 2024-07-12 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_guide', '0002_attraction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('comment', models.CharField(max_length=500)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='city_guide.attraction')),
            ],
        ),
    ]
