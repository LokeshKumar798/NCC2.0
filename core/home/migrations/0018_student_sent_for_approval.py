# Generated by Django 5.1 on 2024-08-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_remove_student_approved_by_brigadier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sent_for_approval',
            field=models.BooleanField(default=False),
        ),
    ]
