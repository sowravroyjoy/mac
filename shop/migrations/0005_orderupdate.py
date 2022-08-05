# Generated by Django 4.0.4 on 2022-07-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=50000)),
                ('Timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
