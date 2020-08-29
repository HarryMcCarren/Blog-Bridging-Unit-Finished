from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
import uuid;

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    class Meta:
        permissions = (("can_see_drafts", "Can view draft posts."),
                        ("can_publish", "Can publish draft posts."), ) 
    
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False);
    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.id)])
    def approve(self):
        self.approved = True
        self.save()
    class Meta:
        permissions = (("can_approve", "Can approve comments."), )