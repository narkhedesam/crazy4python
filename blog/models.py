# import os
# import uuid
from django.db import models
from django.contrib.auth.models import User

# from storages.backends.ftp import FTPStorage
# fs = FTPStorage()

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# def get_upload_path(instance, filename):
#     return os.path.join('blog','images', filename + '_' + str(uuid.uuid4()))

class post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # image = models.ImageField(upload_to='blog\images', blank=True, storage=fs)
    image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    small_description = models.CharField(max_length=200, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    total_views = models.IntegerField(default=0, editable=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)