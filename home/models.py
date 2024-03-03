from django.db import models

class gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="image",blank=True)




    def __str__(self):
        return self.title


