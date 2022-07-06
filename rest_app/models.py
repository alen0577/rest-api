from django.db import models


# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=150)
    task_des = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', default='images/None/noimg.jpg')

    def __str__(self):
        return self.task_name
