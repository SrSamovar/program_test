import pytest
import requests


class TestYandex:
    def setup_method(self):
        self.headers = {
            'Authorization': ''
        }
        self.params = {
            'path': 'image'
        }

    def test_create_folder(self):
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params=self.params, headers=self.headers)
        assert response.status_code == 201

    def test_create_error_folder(self):
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params=self.params, headers=self.headers)
        assert response.status_code == 409
