# Generated by Django 4.0.5 on 2022-08-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_viewer_viewed_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewer',
            name='coins',
            field=models.IntegerField(default=0),
        ),
    ]