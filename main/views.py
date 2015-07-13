from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Bar, Review
from django.core import serializers

def bars(req):
  if req.method == 'POST':
    bar = Bar(yelp_id=req.POST['yelp_id'])
    if bar.is_valid():
      bar.save()
      return HttpResponse("Bar was successfully created")
    else:
      return HttpResponse("Bar was not successfully created")
  else:
    bars = Bar.objects.all()
    data = serializers.serialize('json', bars)
    return HttpResponse(data)

def reviews(req, id):
  if req.method == 'POST':
    bar = get_object_or_404(Bar, id=id)
    print(req.user)
    review = Review(
      rating=req.POST['rating'], 
      comment=req.POST['comment'], 
      bar= bar, 
      user= req.user, 
    )
  else:
    reviews = Review.objects.all()
    data = serializers.serialize('json', reviews)
    return HttpResponse(data)

