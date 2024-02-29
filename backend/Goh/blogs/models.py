from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    auth = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    
    def __str__(self):
        return self.name