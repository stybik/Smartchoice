# Generated by Django 2.0.3 on 2018-04-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestphone', '0002_auto_20180401_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='table_11',
            name='LINK',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]