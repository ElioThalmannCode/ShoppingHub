# Generated by Django 3.0.2 on 2020-01-13 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200108_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart',
            field=models.BooleanField(auto_created=True, default=False),
        ),
    ]
