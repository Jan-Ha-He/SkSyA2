from django.db import models

# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=160)
    deadline = models.DateField()
    progress = models.IntegerField(default=0)
    
    def __str__(self):
        return self.desciption