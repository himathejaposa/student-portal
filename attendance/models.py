from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.course_code} - {self.date}"