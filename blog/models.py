from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images", blank=True)  # Optional image field
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)  # Link to user model
    # Additional optional fields:
    # - category = models.CharField(max_length=50, blank=True)  # Category for the post

    def __str__(self):
        return self.title
