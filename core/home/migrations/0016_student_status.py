# Generated by Django 5.1 on 2024-08-28 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_student_approved_by_brigadier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='Pending approval from Colonel', max_length=100),
        ),
    ]
