from django.db import models

class Team(models.Model):
    
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    job_title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to="teams/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
   
    
    def __str__(self):
        return self.first_name