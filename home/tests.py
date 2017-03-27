from django.test import TestCase, Client
from mock import patch, Mock


class HomeTestCase(TestCase):
    def test_when_home_visited_then_environment_variable_is_valid(self):
        settings_mocked = self.create_mock('home.views.settings')
        settings_mocked.ENV_NAME = 'Test'
        client = Client()
        result = client.get('/')
        self.assertContains(result, "Entorno: Test")

    def create_mock(self, path):
        patcher = patch(path)
        mock = patcher.start()
        self.addCleanup(patcher.stop)
        return mock
