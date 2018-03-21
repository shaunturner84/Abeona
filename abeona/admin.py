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
from .models import Journal
from .models import JournalTag
from .models import JournalPhoto
from .models import Tag

class ReviewFeatureInline(admin.StackedInline):
   model = ReviewFeature

class ReviewPhotoInline(admin.StackedInline):
   model = ReviewPhotos

class JournalTagInline(admin.StackedInline):
   model = JournalTag

class JournalPhotoInline(admin.StackedInline):
   model = JournalPhoto

class ReviewAdmin(admin.ModelAdmin):
   #fieldsets = [
   #  (None, {'fields': ['name','textdata']}),
   #] 
   inlines = [ ReviewFeatureInline, ReviewPhotoInline ]

class JournalAdmin(admin.ModelAdmin):
   inlines = [ JournalTagInline, JournalPhotoInline ]

admin.site.register(PlaceType)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Reviewer)
#admin.site.register(ReviewPhotos)
admin.site.register(Feature)
#admin.site.register(ReviewFeature)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Tag)
