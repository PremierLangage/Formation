from django.urls import path

from apps.todo.views import complete, create, delete, find, index, uncomplete

urlpatterns = [
    path('list', index, name="index"),
    path('find', find, name="index"),
    path('create/', create, name="create"),
    path('complete/<int:id>', complete, name="complete"),
    path('uncomplete/<int:id>', uncomplete, name="uncomplete"),
    path('delete/<int:id>', delete, name="delete"),
]
