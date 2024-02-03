from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
    
    
class Subject(models.Model):
    name = models.CharField(max_length=255)
    teachers = models.ManyToManyField(Teacher, related_name="subjects")

    def __str__(self):
        return f"{self.name} {self.teachers}"


class Class(models.Model):
    grade = models.IntegerField(validators=[
            MaxValueValidator(11),
            MinValueValidator(0)
        ])
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name="school_class")

    def __str__(self):
        return f"{self.grade} {self.teacher}"
    

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    date_birth = models.DateField()
    
    school_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name="students")

    def __str__(self):
        return f"{self.full_name} {self.school_class}"
    
    
class Schedule(models.Model):
    date = models.DateField()
    
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name="schedule")
    school_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name="schedule")

    def __str__(self):
        return f"{self.date} {self.subject} {self.school_class}"
    

class Grade(models.Model):
    grade = models.IntegerField(validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])

    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING, related_name="grades")
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name="grades")

    def __str__(self):
        return f"{self.grade} {self.student} {self.schedule}"
    

    
