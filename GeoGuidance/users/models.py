from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    address = models.CharField(verbose_name="Address",max_lenth= 100, null = True, blank =True)
    town = models.CharField(verbose_name="Address",max_lenth= 100, null = True, blank =True)
    country = models.CharField(verbose_name="country",max_lenth= 100, null = True, blank =True)
    post_code = models.CharField(verbose_name="post_code",max_lenth= 8, null = True, blank =True)
    Longitude = models.CharField(verbose_name="Longitude",max_lenth= 50, null = True, blank =True)
    latitude = models.CharField(verbose_name="latitude",max_lenth= 50, null = True, blank =True)
    county = models.CharField(verbose_name="county",max_lenth= 100, null = True, blank =True)
    
    captcha_score = models.FloatField(default = 0.0)
    has_profile = models.BooleanField(default = False)
    
    is_active = models.BooleanField(default = True)
    
    def __str__(self):
        return f'{self.user}'