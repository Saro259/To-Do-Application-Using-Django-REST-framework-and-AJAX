from django.db import models 



'''The To do app have model of task to invoke the tasks of the day given by the user and also the completion of the task '''
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default= False, blank=True, null=True)

    def __str__(self):
        return self.title
