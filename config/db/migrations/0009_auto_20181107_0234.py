# Generated by Django 2.1.2 on 2018-11-07 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20181107_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='item2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='item3',
            field=models.IntegerField(null=True),
        ),
    ]