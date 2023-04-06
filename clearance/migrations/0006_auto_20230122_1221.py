# Generated by Django 2.2.13 on 2023-01-22 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clearance', '0005_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cleared', 'Cleared'), ('Declined', 'Declined')], default='Pending', max_length=100),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clearance.Department')),
            ],
        ),
    ]