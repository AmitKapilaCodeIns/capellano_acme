from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='course_intro'
    )
    contact_info = models.CharField(max_length=20, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"The name of the course is {self.course_name} and the slug is {self.slug}"


HOLE_NUMBERS = [(i, f"{i}") for i in range(1, 19)]
class HoleGuide(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='holes')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='hole_guides')
    hole_number = models.IntegerField(choices=HOLE_NUMBERS)
    name = models.CharField(max_length=100, blank=True)
    par = models.PositiveSmallIntegerField()
    yardage = models.PositiveIntegerField()
    stroke_index = models.PositiveSmallIntegerField(help_text="1 = hardest hole, 18 = easiest")
    guide = models.TextField(help_text="Strategic tips or description for playing the hole.")
    image = models.ImageField(upload_to='hole_images/', blank=True, null=True)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['hole_number']
        unique_together = ('course', 'hole_number')  # ensures each hole number is unique per course

    def __str__(self):
        return f"{self.course.course_name} - Hole {self.hole_number}"
