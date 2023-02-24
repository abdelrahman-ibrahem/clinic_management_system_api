# Generated by Django 4.1.7 on 2023-02-24 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentReschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Canceled', 'Canceled'), ('Approved', 'Approved'), ('Pendding', 'Pendding')], default='Pendding', max_length=120)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.appointment')),
            ],
        ),
    ]
