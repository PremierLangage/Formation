from django.test import TestCase
from django.urls import reverse
from apps.todo.models import Todo


class TodoTest(TestCase):
    """
    Test case of Todo app
    """

    def setUp(self) -> None:
        Todo.objects.create(task="Task 1", completed=False)
        Todo.objects.create(task="Task 2", completed=True)
        Todo.objects.create(task="Task 3", completed=False)
        Todo.objects.create(task="Task 4", completed=False)


    def test_index(self):
        response = self.client.get(reverse('todo:index'))
        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Task 2')
        self.assertContains(response, 'Task 3')
        self.assertContains(response, 'Task 4')


    def test_create(self):
        response = self.client.post(reverse('todo:create'), data={
            'task': 'Task 5',
            'completed': False
        })
        self.assertRedirects(response, '/', status_code=302)
        todos = Todo.objects.all()
        self.assertEqual(todos.last().task, "Task 5")

    
    def test_complete(self):
        response = self.client.post(reverse('todo:complete', kwargs={"id": 1}))
        self.assertRedirects(response, '/', status_code=302)
        response = self.client.post(reverse('todo:complete', kwargs={"id": 1}))
        self.assertEqual(response.status_code, 400)


    def test_uncomplete(self):
        response = self.client.post(reverse('todo:uncomplete', kwargs={"id": 2}))
        self.assertRedirects(response, '/', status_code=302)
        response = self.client.post(reverse('todo:uncomplete', kwargs={"id": 2}))
        self.assertEqual(response.status_code, 400)


    def test_delete(self):
        todo = Todo.objects.get(id=1)
        response = self.client.post(reverse('todo:delete', kwargs={"id": todo.id}))
        self.assertRedirects(response, '/', status_code=302)
        todos = Todo.objects.all()
        self.assertNotIn(todo, todos)
