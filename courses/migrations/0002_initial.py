# Generated by Django 3.2.12 on 2022-04-02 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur du schedule'),
        ),
        migrations.AddField(
            model_name='parameter',
            name='schedule',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.schedule', verbose_name="schedule de l'object parametres"),
        ),
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.university', verbose_name='Université de la fac'),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.faculty', verbose_name='Faculté du cours'),
        ),
        migrations.AddField(
            model_name='block',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Cours'),
        ),
        migrations.AddField(
            model_name='block',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.schedule', verbose_name='Planning'),
        ),
        migrations.AddField(
            model_name='block',
            name='time_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.timetable', verbose_name='Horaire'),
        ),
    ]
