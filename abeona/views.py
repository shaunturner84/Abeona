# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

from .models import Reviewer
from .models import Review
from .models import ReviewPhotos

def index(request):
   recent_reviews = Review.objects.order_by("-visitdate") [:5]
   rrwi = list()
   for rr in recent_reviews:
     img=''
     ri=ReviewPhotos.objects.filter(reviewid=rr.reviewid).order_by("-reviewphotoid") [:1]
     for rp in ri:
       img=rp.img.url
     rrwi.append({ 'ID': rr.reviewid, 'name': rr.name, 'visitdate': rr.visitdate, 'textdata': rr.textdata, 'rating': rr.rating, 'reviewedby': rr.reviewedby, 'img': img })
   
   template = loader.get_template('abeona/index.html')
   context = {
      'recent_reviews': rrwi
   }
   return HttpResponse(template.render(context, request))


