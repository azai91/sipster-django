from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Bar(models.Model):
  yelp_id = models.CharField(max_length=300)
  review_count = models.IntegerField(default=0)
  happy_times = models.CharField(blank=True, max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
  bar = models.ForeignKey(Bar, related_name='reviews_bar')
  user = models.ForeignKey(User, related_name='reviews_user')
  rating = models.IntegerField()
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

