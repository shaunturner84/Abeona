# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.utils import html
from easy_thumbnails.files import get_thumbnailer

# Create your views here.

from django.http import HttpResponse

from .models import Reviewer
from .models import Review
from .models import ReviewPhotos
from .models import Feature
from .models import ReviewFeature
from .models import Journal
from .models import JournalTag
from .models import JournalPhoto
from .models import Tag

def index(request):
   all_reviews = Review.objects.all()
   template = loader.get_template('abeona/index.html')
   context = {
      'all_reviews': all_reviews
   }
   return HttpResponse(template.render(context, request))

def order_by_date(request):
   all_reviews = Review.objects.all();
   recent_reviews = Review.objects.order_by("-visitdate")
   rrwi = list()
   for rr in recent_reviews:
     img=''
     ri=ReviewPhotos.objects.filter(reviewid=rr.reviewid).order_by("-reviewphotoid") [:1]
     for rp in ri:
       img=rp.img
     rrwi.append({ 'ID': rr.reviewid, 'name': rr.name, 'visitdate': rr.visitdate, 'textdata': rr.textdata, 'rating': rr.rating, 'reviewedby': rr.reviewedby, 'img': img })
   
   template = loader.get_template('abeona/order-by-date.html')
   context = {
      'recent_reviews': rrwi,
      'all_reviews': all_reviews
   }
   return HttpResponse(template.render(context, request))

def journals_by_date(request):
   all_journals = Journal.objects.all();
   recent_journals = Journal.objects.order_by("-entrydate")
   rrwi = list()
   for rr in recent_journals:
     img=''
     ri=JournalPhoto.objects.filter(journalid=rr.journalid).order_by("-journalphotoid") [:1]
     for rp in ri:
       img=rp.img
     rrwi.append({ 'ID': rr.journalid, 'entrydate': rr.entrydate, 'textdata': rr.textdata, 'enteredby': rr.enteredby, 'img': img })

   template = loader.get_template('abeona/journals-by-date.html')
   context = {
      'recent_journals': rrwi,
      'all_journals': all_journals
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

def journal(request, journal_id):
  journal = Journal.objects.filter(journalid=journal_id)[0];
  template = loader.get_template('abeona/journal.html')
  photos = JournalPhoto.objects.filter(journalid=journal.journalid)
  tags = JournalTag.objects.filter(journalid=journal.journalid)
  textdata = html.format_html(journal.textdata)
  context = {
     'journal': journal,
     'journal_id': journal_id,
     'photos': photos,
     'tags': tags,
     'textdata': journal.textdata
  }
  return HttpResponse(template.render(context, request));


