from django.db import models


# Create your models here.
class Intro_video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(
        upload_to="Intro_video", default="Image/profile1.png", null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to="Testimonials", default="Image/profile1.png", null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    facebook_link = models.URLField(max_length=1000, default="raise.recb.ac.in", null=True, blank=True)
    twitter_link = models.URLField(max_length=1000, default="raise.recb.ac.in", null=True, blank=True)
    linkedin_link = models.URLField(max_length=1000, default="raise.recb.ac.in", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
