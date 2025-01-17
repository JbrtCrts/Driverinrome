# Generated by Django 5.1.1 on 2024-10-11 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rate', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Date_Rate',
            fields=[
                ('Date', models.DateField(primary_key=True, serialize=False)),
                ('Rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Price_Rate', to='Quoter.rate')),
            ],
        ),
    ]
