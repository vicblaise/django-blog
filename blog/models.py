from django.db import models
from djanjo.contrib.auth.models import user
STATUS = ((0,"Draft"), (1, "published"))

# Create your models here.
class Post(models. Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        user, on_delete=models.CASCADE,releted_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)