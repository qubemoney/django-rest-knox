# Generated by Django 3.2.12 on 2022-05-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0009_authtoken_token_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='token_type',
            field=models.CharField(choices=[('mobile', 'mobile'), ('trusted_web', 'trusted_web'), ('web', 'web')], default='web', max_length=32),
        ),
    ]