# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.utils import html

# Create your views here.

from django.http import HttpResponse

from .models import Reviewer
from .models import Review
from .models import ReviewPhotos
from .models import Feature
from .models import ReviewFeature

def index(request):
   all_reviews = Review.objects.all()
   template = loader.get_template('abeona/index.html')
   context = {
      'all_reviews': all_reviews
   }
   return HttpResponse(template.render(context, request))

def order_by_date(request):
   all_reviews = Review.objects.all();
   recent_reviews = Review.objects.order_by("-visitdate") [:5]
   rrwi = list()
   for rr in recent_reviews:
     img=''
     ri=ReviewPhotos.objects.filter(reviewid=rr.reviewid).order_by("-reviewphotoid") [:1]
     for rp in ri:
       img=rp.img.url
     rrwi.append({ 'ID': rr.reviewid, 'name': rr.name, 'visitdate': rr.visitdate, 'textdata': rr.textdata, 'rating': rr.rating, 'reviewedby': rr.reviewedby, 'img': img })
   
   template = loader.get_template('abeona/order-by-date.html')
   context = {
      'recent_reviews': rrwi,
      'all_reviews': all_reviews
   }
   return HttpResponse(template.render(context, request))

def review(request, review_id):
  review = Review.objects.filter(reviewid=review_id)[0];
  template = loader.get_template('abeona/review.html')
  photos = ReviewPhotos.objects.filter(reviewid=review.reviewid)
  features = ReviewFeature.objects.filter(reviewid=review.reviewid)
  textdata = html.format_html(review.textdata)
  context = {
     'review': review,
     'review_id': review_id,
     'photos': photos,
     'features': features,
     'textdata': review.textdata
  }
  return HttpResponse(template.render(context, request));

