from django.db import models

# Create your models here.
class Bar(models.Model):
  yelp_id = models.CharField(required=True)
  review_count = models.IntegerField(default=0)
  happy_times = models.CharField()