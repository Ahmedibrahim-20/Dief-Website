from django.db import models

# Create your models here.

class Images(models.Model):
    
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="blog-images/")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

