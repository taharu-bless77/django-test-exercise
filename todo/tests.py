from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from todo.models import Task

class TaskModelTestCase(TestCase):
    def test_create_task1(self):
        # テスト用の締切日時データを作成
        due = timezone.make_aware(datetime(2024, 6, 30, 23, 59, 59))

        # データベースにタスクを作成して保存
        task = Task(title='task1', due_at=due)
        task.save()

        # データベースから今保存したタスクを再度取得
        task = Task.objects.get(pk=task.pk)

        # 取得したタスクの各フィールドが期待通りの値かチェック
        self.assertEqual(task.title, 'task1')
        self.assertFalse(task.completed)
        self.assertEqual(task.due_at, due)