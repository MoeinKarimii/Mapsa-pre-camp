from django.db import models
from django.utils import timezone
from django.forms import ValidationError
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True)

    def __str__(self):
        return self.name


def error_for_time(value):
    if value > timezone.now():
        return value
    raise ValidationError("The time you have chosen as deadline is not valid")


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, validators=[error_for_time])
    check_box = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category}-{self.title}"
