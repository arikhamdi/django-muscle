from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils.safestring import mark_safe
from tinymce import HTMLField


class Category(models.Model):
    TYPE = (
        ('Body Building', 'Body Building'),
        ('Aerobic', 'Aerobic'),
        ('Weight Lifting', 'Weight Lifting'),
        ('Yoga', 'Yoga'),
    )
    category = models.CharField(max_length=100, choices=TYPE)

    def __str__(self) -> str:
        return self.category


class Exercise(models.Model):
    image = models.ImageField(upload_to='exercises')
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = HTMLField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('workouts:exercise_detail', kwargs={
            'exercise_id': self.id
        })


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True, upload_to='members')

    def __str__(self) -> str:
        return self.user.username


class Banner(models.Model):
    image = models.ImageField(upload_to='banner')

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" style="width: 250px;" />')
