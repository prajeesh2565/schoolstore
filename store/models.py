from django.db import models

# Create your models here.

class department(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class courses(models.Model):
    course_name = models.CharField(max_length=100,unique=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name