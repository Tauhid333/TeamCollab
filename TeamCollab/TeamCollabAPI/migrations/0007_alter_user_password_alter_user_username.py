# Generated by Django 5.0.6 on 2024-06-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamCollabAPI', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
