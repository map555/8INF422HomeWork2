# Generated by Django 3.1.2 on 2020-10-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TP2Q3', '0002_auto_20201015_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(choices=[('1', 'very bad'), ('2', 'bad'), ('3', 'normal'), ('4', 'good'), ('5', 'very good'), ('6', 'showroom')], default=('3', 'normal'), max_length=1),
        ),
    ]
