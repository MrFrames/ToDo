from django.db import models

# Create your models here.
# Database structure here

class Task(models.Model):

    def __str__(self):
        return self.task_name

    task_name = models.CharField(max_length=200)
    task_priority = models.CharField(max_length=200)
    task_info = models.CharField(max_length=200)
    task_done = models.CharField(max_length=4)

    def done(self):
        self.task_done.set('done')