from django.test import TestCase
from accounts.models import Cliente
from django.contrib.auth.models import User

class ClienteTestCase(TestCase):

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