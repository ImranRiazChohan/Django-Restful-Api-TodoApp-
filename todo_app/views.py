from django.shortcuts import render
from .models import Task
from .serialization import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# {
#     "id": 3,
#     "title": "Learn Django Rest_FrameWork",
#     "completed": false
# }

@api_view(["GET"])
def apioverview(request):
    api_urls={
        "Home":"Rest FrameWork",
        "List":"/task_list/",
        "Detail view":"/task_detail/<str:pk>/",
        "Create":"/task_create/",
        "Update":"/task_update/<str:pk>/",
        "Delete":"/task_delete/<str:pk>/",
    }
    return Response(api_urls)
@api_view(["GET"])
def tasklist(request):
    task=Task.objects.all()
    serializer=TaskSerializer(task,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def task_detail(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def task_create(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def task_delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response("Task has been Deleted Successfully!")
@api_view(["PUT"])
def task_update(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




