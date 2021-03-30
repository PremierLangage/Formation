from django.urls import path

from apps.todo.views import complete, create, delete, index, uncomplete

urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('complete/<int:id>', complete, name="complete"),
    path('uncomplete/<int:id>', uncomplete, name="uncomplete"),
    path('delete/<int:id>', delete, name="delete"),
]
