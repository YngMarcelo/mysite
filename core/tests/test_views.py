# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class IndexViewTestCase(TestCase):

    #teste setup será usado para todos os testes afim de evitar repetições

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')
    #teste teardown fecha o teste
    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')
