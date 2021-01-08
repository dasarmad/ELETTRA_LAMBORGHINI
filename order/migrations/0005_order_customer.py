# Generated by Django 3.1.4 on 2021-01-03 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0005_auto_20201214_1708'),
        ('order', '0004_auto_20210103_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agents.customer'),
        ),
    ]