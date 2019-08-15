import datetime
from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=8)
    saved_date = models.DateTimeField('date added')

    def __str__(self):
        return self.name+self.surname+str(self.age)+self.gender+str(self.saved_date)

    def was_added_recently(self):
        return self.saved_date >= timezone.now() - datetime.timedelta(days=1)

    