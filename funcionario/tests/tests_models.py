from django.test import TestCase
from funcionario.models import Funcionario

class FuncionarioModelsTestCase(TestCase):

    def test_create_empresa(self):
        funcionario = Funcionario.objects.create(
            nome = "Mark Down",
            username = "md"
        )

        self.assertEqual(funcionario.nome, "Mark Down")
        self.assertNotEqual(funcionario.username, 'mg')