import uuid 
from django.db import models
from django.utils import timezone
from accounts.models import User
from django.urls import reverse

class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250) # VARCHAR in SQL
    slug = models.SlugField(max_length=250) # VARCHAR in SQL
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField() # Text in SQL
    publish = models.DateTimeField(default=timezone.now) # DATETIME in SQL
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishManager()

    class Meta:
        db_table = 'posts'
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
                                                 self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug,
                                                 self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'comments'
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'