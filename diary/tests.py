from django.test import TestCase
from django.urls import reverse

from diary.models import Record
from users.models import User


class RecordTestCase(TestCase):
    """Тест CRUD записей."""

    def setUp(self):
        """Создание тестового пользователя для авторизации."""

        self.user = User.objects.create(email="admin2026@example.com")
        self.user.set_password("testpassword123")
        self.user.save()

        self.record = Record.objects.create(
            owner=self.user,
            date="2026-01-08",
            contents="День прошел замечательно!",
        )

        self.client.login(username="admin2026@example.com", password="testpassword123")

    def test_detail_record(self):
        """Тест вывод записи."""

        url = reverse("diary:record_detail", args=(self.record.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_record(self):
        """Тест создания записи."""

        url = reverse("diary:record_create")
        data = {
            "date": "2026-01-09",
            "contents": "День прошел хорошо!",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Record.objects.filter(contents="День прошел хорошо!").exists())

    def test_update_record(self):
        """Тест обновления записи."""

        url = reverse("diary:record_update", args=(self.record.pk,))
        data = {
            "date": "2026-01-08",
            "contents": "День прошел плохо!",
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.record.refresh_from_db()
        self.assertEqual(self.record.contents, "День прошел плохо!")

    def test_delete_record(self):
        """Тест удаления записи."""

        url = reverse("diary:record_delete", args=(self.record.pk,))
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Record.objects.filter(pk=self.record.pk).exists())
