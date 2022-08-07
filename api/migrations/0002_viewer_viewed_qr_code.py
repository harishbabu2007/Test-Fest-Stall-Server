# Generated by Django 4.0.5 on 2022-08-04 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('class_user', models.CharField(max_length=500)),
                ('section', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Viewed_Qr_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.qrcodes')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.viewer')),
            ],
        ),
    ]
