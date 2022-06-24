from django.db import models

STATUS_CH = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Задачи")
    author = models.CharField(max_length=50, verbose_name="Автор", default="Unknown")
    content = models.TextField(max_length=2000, verbose_name="Контент")
    date = models.DateField(max_length=30, null=True, blank=True, verbose_name="Дата")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=20, choices=STATUS_CH, default=STATUS_CH[0][0], verbose_name="Статус")


    def __str__(self):
        return f"{self.id}. {self.title} : {self.author}"

    class Meta:
        db_table = "articles"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


