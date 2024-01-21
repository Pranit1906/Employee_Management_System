# Generated by Django 5.0.1 on 2024-01-21 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('floor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('designation', models.CharField(choices=[('Associate', 'Associate'), ('TL', 'TL'), ('Manager', 'Manager')], max_length=25)),
                ('departments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='emsApp.department')),
                ('reporting_manager', models.ForeignKey(blank=True, choices=[('TL', 'TL'), ('Manager', 'Manager')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='emsApp.employee')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='managers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='emsApp.employee'),
        ),
        migrations.CreateModel(
            name='Employee_Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('from_Date', models.DateField()),
                ('till_Date', models.DateField()),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='emsApp.employee')),
            ],
        ),
    ]