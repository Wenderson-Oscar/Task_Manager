from django.test import TestCase
from accounts.models import Cliente
from django.contrib.auth.models import User
from .forms import ClienteForm
from django.urls import reverse


class ClientModelTestCase(TestCase):

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
        
    def test_cliente_str(self):

        self.assertEqual(str(self.cliente.user), self.user.username)
        self.assertEqual(str(self.cliente), self.user.email)
        self.assertEqual(str(self.cliente.user.password), self.user.password)
        self.assertEqual(str(self.cliente.sexo), 'M')
        self.assertEqual(str(self.cliente.nascimento), '2000-01-01')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)


class ClienteFormTestCase(TestCase):
    
    def test_valid_form(self):

        form_data = {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password1': '32#aWasdfr@',
            'password2': '32#aWasdfr@',
            'sexo': 'M',
            'nascimento': '2000-01-01'
        }

        form = ClienteForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        
    def test_save_method(self):

        form_data = {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password1': '32#aWasdfr@',
            'password2': '32#aWasdfr@',
            'sexo': 'M',
            'nascimento': '2000-01-01'
        }

        form = ClienteForm(data=form_data)        
        self.assertTrue(form.is_valid(), form.errors)
        user = form.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, form_data['username'])
        self.assertEqual(user.email, form_data['email'])
        cliente = Cliente.objects.get(user=user)
        self.assertEqual(cliente.sexo, form_data['sexo'])
        self.assertEqual(cliente.nascimento.strftime('%Y-%m-%d'), form_data['nascimento'])


class DelAccountViewsTestCase(TestCase):

    def setUp(self) -> None:
        
        self.user = User.objects.create_user(
            username='Teste@',
            email='teste@gmail.com',
            password='1@Weqasd9'
            )

    def confirmed_delete_account(self):

        self.client.login(username=self.user.email, password=self.user.password)
        url = reverse('confirm_delete_client')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tem certeza que deseja excluir a Conta ?')

    def test_delete_account(self):
        
        self.client.login(username=self.user.email, password=self.user.password)
        url = reverse('delete_client')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username=self.user.email).exists())