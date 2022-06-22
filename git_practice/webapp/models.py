from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    author = models.CharField(max_length=50, verbose_name="Заголовок", default="Unknown")
    content = models.TextField(max_length=2000, verbose_name="Контент")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.id}. {self.title} : {self.author}"

    class Meta:
        db_table = "articles"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


