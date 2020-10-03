from django.test import TestCase
from empresa.models import Empresa

class EmpresaModelsTestCase(TestCase):

    def test_create_empresa(self):
        empresa = Empresa.objects.create(
            nome="Company and Hero",
            cnpj="12345/3"
        )

        self.assertEqual(empresa.nome, "Company and Hero")
        self.assertNotEqual(empresa.cnpj, '231/453')