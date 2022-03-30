from django.db import models

class Todo(models.Model):
    The_Job = models.CharField(max_length=1000)
    Check = models.BooleanField()

    def __str__(self) ->str:
        return self.The_Job