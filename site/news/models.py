from django.db import models

class contents(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    writer = models.CharField(max_length=10)
