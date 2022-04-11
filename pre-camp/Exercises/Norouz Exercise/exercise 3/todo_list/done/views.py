from django.shortcuts import render
from django.http import JsonResponse

from .models import Todo


def list_of_todo(requset):
    qs = Todo.objects.all()
    result = []
    temp = {}
    for elm in qs:
        temp["The_Job"] = elm.The_Job
        temp["Check"] = elm.Check
        result.append(temp)
    return JsonResponse(result, safe=False)

