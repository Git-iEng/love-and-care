from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True, null=True) 
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"
