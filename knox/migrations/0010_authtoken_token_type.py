from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0009_authtoken_token_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='token_type',
            field=models.CharField(choices=[('web', 'web'), ('mobile', 'mobile'), ('trusted_web', 'trusted_web'),], default='web', max_length=32),
        ),
    ]
