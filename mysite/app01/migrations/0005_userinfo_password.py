# Generated by Django 3.2.18 on 2023-07-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_alter_userinfo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default=12, max_length=64),
            preserve_default=False,
        ),
    ]
