# Generated by Django 3.0.8 on 2020-10-31 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20201031_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='anonymous',
            field=models.BooleanField(),
        ),
    ]
