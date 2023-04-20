from django.contrib.auth.models import User
from django.db import models

# Campus class to store the name of the campus

class Campus(models.Model):
    identifier = models.CharField(max_length=255)

# Program class to store the program each student is enrolled in. 

class Program(models.Model):
    identifier = models.CharField(max_length=255)

# Student class to store student's data i.e first name, last name etc. 
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    gpa = models.FloatField()

#Student Program to store the priority of each program the student is enrolled in.
class StudentProgram(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    priority_order = models.IntegerField()