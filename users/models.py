from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class User(AbstractUser):
    user_types = (
        ('admin', 'Admin'),
        ('prof', 'Professor'),
        ('student', 'Student'),
    )

    accountType = models.CharField(choices=user_types, default="student", blank=False, max_length=10)
    courses = models.ManyToManyField("courses.Course", verbose_name="Cours suivits", through="users.StudentToCourse")


class StudentToCourse(models.Model):

    status_choices = (
        ('running', 'En cours'),
        ('succeeded', 'Réussi'),
        ('failed', 'Raté'),
    )

    student = models.ForeignKey("users.User", verbose_name="Etudiant", on_delete=models.CASCADE)
    course = models.ForeignKey("courses.Course", verbose_name="Cours", on_delete=models.CASCADE)
    status = models.CharField(choices=status_choices, max_length=10, default="running")
    grade = models.PositiveIntegerField(default=0, verbose_name="Grade")
    participation_to_the_course = models.BooleanField("A participé au cours", default=False)
    difficulty = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(10), MinValueValidator(1)], verbose_name="Difficulty")