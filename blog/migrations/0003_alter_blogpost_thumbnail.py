# Generated by Django 4.0.4 on 2022-08-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_chead0_blogpost_chead1_blogpost_chead2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]