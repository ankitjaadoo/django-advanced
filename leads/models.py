from django.db import models

# Create your models here.

class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YT','Youtube'),
        ('Goog','Google'),
        ('NewsLetter','NewsLetter')
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES,max_length=100)
    
    profile_picture = models.ImageField(blank=True,null=True)
    special_files = models.FileField(blank=True,null=True)
    