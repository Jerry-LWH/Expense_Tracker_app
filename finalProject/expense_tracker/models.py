from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    
from django.utils import timezone

# Create your models here.

class UserProfileInfo(models.Model):
    """This class creates a user's profile account."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        """This function returns the user's username."""
        return self.user.username

class Transactions(models.Model):
    """This class creates a transactions model that can be paired up with a user for the expanse model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, blank = True)

    category = models.CharField(max_length=200)
    payee = models.CharField(default='gas',max_length=200)
    description = models.CharField(max_length =200)
    amounts = models.IntegerField(default=0)
    def __str__(self):
        """This function returns the category."""
        return self.category


class Envelop(models.Model):
    """This class creates an envelop model that can be paired up with a user for the expanse model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_day = models.IntegerField(default=1)
    category = models.CharField(max_length=200)
    amounts = models.IntegerField(default=0)
    def __str__(self):
        """This function returns the category."""
        return self.category
