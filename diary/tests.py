from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from diary.models import Record
from users.models import User


class RecordTestCase(APITestCase):
    """Тест CRUD записей."""

    def setUp(self):
        """Создание тестового пользователя для авторизации."""
        self.user = User.objects.create(email="admin2026@example.com")

        self.record = Record.objects.create(
            owner=self.user,
            date="2026-01-08",
            contents="День прошел замечательно!",
        )

        self.client.force_authenticate(user=self.user)

    def test_detail_record(self):
        """Тест вывод записи."""
        client = APIClient()
        response = client.post('/login/', data={'username': 'admin2026@example.com', 'password': '25102024'})
        client.credentials(HTTP_AUTHORIZATION='Token ' + '09602c0ec060a3cc20d959e11c911607')
        url = f'/diary/{self.record.pk}/'
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # url = reverse("diary:record_detail", args=(self.record.pk,))
        # response = self.client.get(url)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_record(self):
        """Тест создания записи."""
        client = APIClient()
        response = client.post('/login/', data={'username': 'admin2026@example.com', 'password': '25102024'})
        client.credentials(HTTP_AUTHORIZATION='Token ' + '09602c0ec060a3cc20d959e11c911607')
        url = reverse("diary:record_create")
        data = {
            "owner": self.user.id,
            "date": "2026-01-08",
            "contents": "День прошел хорошо!",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_update_record(self):
        """Тест обновления записи."""
        url = reverse("diary:record_update", args=(self.record.pk,))
        data = {
            "contents": "День прошел плохо!",
        }

        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_record(self):
        """Тест удаления записи."""
        url = reverse("diary:record_delete", args=(self.record.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


