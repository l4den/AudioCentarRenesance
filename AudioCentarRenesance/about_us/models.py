from django.db import models

class AboutUsImage(models.Model):
    image = models.ImageField(upload_to='about_us_photos')


class AboutUsText(models.Model):
    text = models.TextField()


