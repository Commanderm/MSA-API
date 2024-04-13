import unittest
from unittest.mock import patch
from task_service import app

class TestTaskService(unittest.TestCase):

    def test_create_task(self):
        # Мокаем метод отправки данных в БД или внешний сервис
        with patch('task_service.create_task') as mock_create_task:
            # Вызываем метод создания задачи
            app.create_task(description='Test task')

            # Проверяем, что метод был вызван с правильными аргументами
            mock_create_task.assert_called_once_with(description='Test task')

        # Добавим вывод сообщения об успешном прохождении теста
        print("Unit test 'test_create_task' passed successfully!")


if __name__ == '__main__':
    unittest.main()