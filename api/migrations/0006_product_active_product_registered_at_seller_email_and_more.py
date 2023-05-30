# Generated by Django 4.1.5 on 2023-05-30 03:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_buyer_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='registered_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 30, 9, 29, 21, 747333)),
        ),
        migrations.AddField(
            model_name='seller',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='seller',
            name='password',
            field=models.CharField(default='password', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.seller'),
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
    ]