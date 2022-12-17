from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=25)
    def __str__(self):
        return self.category_name

class NewsStory(models.Model):
    class Meta:
        ordering = ['-pub_date'] #added for ordering dates

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField()
    newsCategory = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)


