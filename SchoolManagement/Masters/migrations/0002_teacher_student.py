# Generated by Django 4.2.3 on 2023-07-21 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ClassManagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Masters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Others', 'Others')], default='Male', max_length=50)),
                ('DOB', models.DateField(default='1980-01-01')),
                ('dept', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Masters.department')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Others', 'Others')], default='Male', max_length=50)),
                ('DOB', models.DateField(default='1998-01-01')),
                ('class_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ClassManagement.class')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
