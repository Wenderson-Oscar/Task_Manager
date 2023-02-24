from django.test import TestCase
from task_management.models import Tarefa
from accounts.models import Cliente
from django.contrib.auth.models import User
from django.utils import timezone
from task_management.forms import TaskForms


class TaskModelTestCase(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create_user(
            username='Teste@',
            email='teste@gmail.com',
            password='1@Weqasd9'
            )

        self.cliente = Cliente.objects.create(
            user = self.user,
            sexo = 'M',
            nascimento = '2000-01-01'
        )

        self.task = Tarefa.objects.create(
            titulo = 'Teste',
            descricao = 'Teste Descrição',
            data_criacao = timezone.now(),
            data_conclusao = '2023-06-20',
            status = 'Pendente',
            user = self.cliente
        )

    def test_create_task_successfully(self):

        self.client.login(username=self.user.email, password=self.user.password)
        self.assertEqual(self.task.titulo, 'Teste')
        self.assertEqual(self.task.descricao, 'Teste Descrição')
        self.assertTrue(self.task.data_criacao)
        self.assertEqual(self.task.data_conclusao, '2023-06-20')
        self.assertEqual(self.task.status, 'Pendente')
        self.assertEqual(self.task.user, self.cliente)

    def test_edit_task_changes_properties(self):

        self.client.login(username=self.user.email, password=self.user.password)
        self.task.titulo = 'Teste editado'
        self.task.descricao = 'Teste Descrição editada'
        self.task.data_conclusao = '2023-06-21'
        self.task.status = 'Concluída'
        self.task.save()
        self.assertEqual(self.task.titulo, 'Teste editado')
        self.assertEqual(self.task.descricao, 'Teste Descrição editada')
        self.assertEqual(self.task.data_conclusao, '2023-06-21')
        self.assertEqual(self.task.status, 'Concluída')

    def test_delete_task_removes_task_from_database(self):

        self.client.login(username=self.user.email, password=self.user.password)
        task_id = self.task.id
        response = self.client.post(f'/task/task/{task_id}/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Tarefa.objects.filter(id=task_id).exists())


class TaskFormTestCase(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create_user(
            username='Teste@',
            email='teste@gmail.com',
            password='1@Weqasd9'
            )

        self.cliente = Cliente.objects.create(
            user = self.user,
            sexo = 'M',
            nascimento = '2000-01-01'
        )

    def test_valid_form(self):

        form_data = {
            'titulo': 'Teste',
            'descricao': 'teste descrição',
            'data_conclusao': '2023-06-20',
            'status': 'Pendente',
            'user': self.cliente
        }

        form = TaskForms(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_save_method(self):
    
        form_data = {
            'titulo': 'Teste',
            'descricao': 'teste descrição',
            'data_conclusao': '2023-06-20',
            'status': 'Pendente',
            'user': self.cliente
        }

        form = TaskForms(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        task = form.save(commit=False)
        task.user = self.cliente
        task = form.save()
        self.assertEqual(task.titulo, form_data['titulo'])
        self.assertEqual(task.descricao, form_data['descricao'])
        self.assertEqual(task.data_conclusao.strftime('%Y-%m-%d'), form_data['data_conclusao'])
        self.assertEqual(task.status, form_data['status'])
        self.assertEqual(task.user, self.cliente)
