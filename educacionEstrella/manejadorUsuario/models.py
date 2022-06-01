from django.db import models
from django.contrib.auth.models import User
# Create your models here. 

# Extending User Model Using a One-To-One Link
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    '''

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
   ip_address = models.GenericIPAddressField(null=True)
   def __str__(self):
        return self.user.username