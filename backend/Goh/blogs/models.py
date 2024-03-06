from django.db import models
from django.contrib.auth import get_user_model

# class Category(models.Model):
#     name = models.CharField(max_length = 100)
    
#     def __str__(self):
#         return self.name
# class Tag(models.Model):
#     name = models.CharField(max_length = 100)
#     def __str__(self):
#         return self.name
User = get_user_model()

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200, default = "admin" )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    category = models.CharField(max_length = 200, default = "development")
    tags = models.CharField(max_length = 200, default = "#Django, Docker")
    image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    
    def __str__(self):
        return self.title