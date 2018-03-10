# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import PlaceType
from .models import Review
from .models import Reviewer
from .models import ReviewPhotos

admin.site.register(PlaceType)
admin.site.register(Review)
admin.site.register(Reviewer)
admin.site.register(ReviewPhotos)
