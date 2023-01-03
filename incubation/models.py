from django.db import models


# Create your models here.
class Slider(models.Model):
    image = models.ImageField(
        upload_to="Slider", default="Image/hero-area.jpg", null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.image


class Supported_By(models.Model):
    image = models.ImageField(
        upload_to="Supported_By", default="Image/hero-area.jpg", null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.image


class Link(models.Model):
    google_form_link = models.URLField(default="#", null=True, blank=True)
    intro_video_link = models.URLField(default="#", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.id


class Partner(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    comment = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to="Partners", default="Image/profile1.png", null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    facebook_link = models.URLField(max_length=1000, default="raiseb.recb.ac.in", null=True, blank=True)
    twitter_link = models.URLField(max_length=1000, default="raiseb.recb.ac.in", null=True, blank=True)
    linkedin_link = models.URLField(max_length=1000, default="raiseb.recb.ac.in", null=True, blank=True)
    image = models.ImageField(
        upload_to="Team", default="Image/profile1.png", null=True, blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
