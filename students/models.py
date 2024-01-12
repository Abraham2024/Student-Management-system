from django.db import models

# Create your models here.

class Students (models.Model):
    Student_name = models.PositiveIntegerField()
    First_name = models.CharField(max_length = 50)
    Last_name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length = 50)
    Field_of_study = models.CharField(max_length = 50)
    gpa = models.FloatField()

    def __str__(self):
        return f'student: {self.first_name} {self.last_name}'

