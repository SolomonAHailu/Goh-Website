from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200 )
    email = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.first_name