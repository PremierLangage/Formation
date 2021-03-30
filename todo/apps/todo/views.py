import json
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http.response import JsonResponse
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
def find(request, id):
    try:
        todo = Todo.objects.get(id=id)
        return JsonResponse({
            "id": todo.id,
            "task": todo.task,
            "completed": todo.completed
        })
    except Todo.DoesNotExist:
        return HttpResponseNotFound('Task does not exist!')



@require_POST
@csrf_exempt
def create(request):
    form = json.loads(request.body)
    
    todo = Todo.objects.create(
        task=form.get("task"),
        completed=form.get("completed")
    )

    return JsonResponse({
        "id": todo.id,
        "task": todo.task,
        "completed": todo.completed
    })


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
    return JsonResponse({ "success": True })


@require_POST
@csrf_exempt
def delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse({ "success": True })
    except Todo.DoesNotExist:
        return HttpResponseNotFound('Task does not exist!')