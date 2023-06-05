from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Profile(models.Model):
  username = models.ForeignKey(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100, blank=True)
  last_name = models.CharField(max_length=100, blank=True)

  class Meta:
    db_table = 'db_profiles'
    managed = True
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'

  def __str__(self):
      return self.username
  

class Interest(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, blank=False)

  class Meta:
    db_table = 'db_interests'
    managed = True
    verbose_name = 'Interest'
    verbose_name_plural = 'Interests'

  def __str__(self):
      return self.name
  

class PickedInterests(models.Model):
  interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
  user =  models.ForeignKey(Profile, on_delete=models.CASCADE)