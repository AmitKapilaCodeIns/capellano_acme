from django.db import models

# Create your models here.
class About(models.Model):
    """
    Stores information about the site author
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    # profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        return self.title