# Generated by Django 2.1.2 on 2018-11-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0018_order_noofitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderType',
            field=models.CharField(choices=[('N', 'New'), ('D', 'Dequeued')], default='N', max_length=200),
        ),
    ]
