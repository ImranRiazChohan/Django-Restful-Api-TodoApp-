from django.urls import path
from . import views


urlpatterns=[
    path("",views.apioverview,name="api-overview"),
    path("task_list/",views.tasklist,name="task_list"),
    path("task_detail/<str:pk>/",views.task_detail,name="task_detail"),
    path("task_create/",views.task_create,name="create_task"),
    path("task_delete/<str:pk>/", views.task_delete, name="delete_task"),
    path("task_update/<str:pk>/", views.task_update, name="update_task"),


]