from django.db import models


class Icon(models.Model):
    icon = models.ImageField(upload_to="projects/", blank= True, null=True)
    
    
class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    icon = models.ManyToManyField(Icon)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
   
    
    def __str__(self):
        return self.title