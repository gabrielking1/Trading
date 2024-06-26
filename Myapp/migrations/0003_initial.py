# Generated by Django 4.0 on 2023-06-01 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Myapp', '0002_delete_entry_delete_trader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capital', models.FloatField(default=100.0)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit_loss', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='Myapp.trader')),
            ],
        ),
    ]
