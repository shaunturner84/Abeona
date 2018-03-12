# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import PlaceType
from .models import Review
from .models import Reviewer
from .models import ReviewPhotos
from .models import Feature
from .models import ReviewFeature

class ReviewFeatureInline(admin.StackedInline):
   model = ReviewFeature

class ReviewPhotoInline(admin.StackedInline):
   model = ReviewPhotos

class ReviewAdmin(admin.ModelAdmin):
   #fieldsets = [
   #  (None, {'fields': ['name','textdata']}),
   #] 
   inlines = [ ReviewFeatureInline, ReviewPhotoInline ]

admin.site.register(PlaceType)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Reviewer)
#admin.site.register(ReviewPhotos)
admin.site.register(Feature)
#admin.site.register(ReviewFeature)
