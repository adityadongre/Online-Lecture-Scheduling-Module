from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')

class Lecture(models.Model):
    date = models.DateField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
