from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from apps.todo.forms import TodoForm
from apps.todo.models import Todo
from django.views.decorators.csrf import csrf_exempt



@require_GET
def index(request):
    todos = Todo.objects.all()
    response = []
    for e in todos:
        response.append({
            "id": e.id,
            "task": e.task,
            "completed": e.completed
        })
    return JsonResponse(response, safe=False)


@require_POST
@csrf_exempt
def create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ('Task has been added!'))
        return JsonResponse({ "success": True })

    return HttpResponseBadRequest('Task form is not valid')


@require_POST
@csrf_exempt
def complete(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return HttpResponseNotFound('Task does not exist!')
    
    if todo.completed:
        return HttpResponseBadRequest('Task is already completed!')

    todo.completed = True
    todo.save()
    messages.success(request, ('Task has been marked as complete!'))
    return JsonResponse({ "success": True })


@require_POST
@csrf_exempt
def uncomplete(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return HttpResponseNotFound('Task does not exist!')

    if not todo.completed:
        return HttpResponseBadRequest('Task is not completed!')
    
    todo.completed = False
    todo.save()
    messages.success(request, ('Task has been marked as uncomplete!'))
    return JsonResponse({ "success": True })


@require_POST
@csrf_exempt
def delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return HttpResponseNotFound('Task does not exist!')

    todo.delete()
    messages.success(request, ('Task has been Deleted!'))
    return JsonResponse({ "success": True })
