from django.db import models

class AboutUsImage(models.Model):
    image = models.ImageField(upload_to='about_us_photos')

    def __str__(self):
        return 'About us image'


class AboutUsText(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField()

    def __str__(self):
        return 'About us Title and Description' 


