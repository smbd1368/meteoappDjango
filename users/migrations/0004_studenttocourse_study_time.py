# Generated by Django 3.2.12 on 2022-04-02 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_participation_to_the_course_studenttocourse_attended'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttocourse',
            name='study_time',
            field=models.PositiveBigIntegerField(default=0, verbose_name='study_time'),
        ),
    ]
