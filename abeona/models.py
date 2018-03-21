# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.dispatch import receiver
from easy_thumbnails.signals import saved_file
from abeona import tasks

# Create your models here.

@receiver(saved_file)
def generate_thumbnails_async(sender, fieldfile, **kwargs):
    tasks.generate_thumbnails.delay(
        model=sender, pk=fieldfile.instance.pk,
        field=fieldfile.field.name)

@python_2_unicode_compatible
class PlaceType(models.Model):
   placetypeid = models.AutoField(primary_key=True)
   name = models.CharField(max_length=20,default='<Place Name>')
   def __str__(self):
     return self.name
   class Meta:
     ordering = ( 'name', )

@python_2_unicode_compatible
class Reviewer(models.Model):
   reviewerid = models.AutoField(primary_key=True)
   name = models.CharField('Name of Reviewer', max_length=20, default='<Name of Reviewer>')
   def __str__(self):
     return self.name
   class Meta:
     ordering = ( 'name', )

   
@python_2_unicode_compatible
class Review(models.Model):
   reviewid = models.AutoField(primary_key=True)
   name = models.CharField('Where are you reviewing',max_length=200,default='<name of place')
   reviewedby = models.ForeignKey(Reviewer,null=True,on_delete=models.CASCADE)
   placetypeid = models.ForeignKey(PlaceType, on_delete=models.CASCADE)
   visitdate = models.DateTimeField('Date of Visit',default=timezone.now)
   rating = models.DecimalField(null=True,max_digits=3,decimal_places=1)
   textdata = models.TextField(null=True)
   lat= models.DecimalField(null=True,max_digits=10,decimal_places=6)
   lng= models.DecimalField(null=True,max_digits=10,decimal_places=6)
   def __str__(self):
     return str(self.name)
   class Meta:
     ordering = ( '-visitdate', )

@python_2_unicode_compatible
class ReviewPhotos(models.Model):
   reviewphotoid = models.AutoField(primary_key=True)
   reviewid = models.ForeignKey(Review,on_delete=models.CASCADE)
   description = models.CharField(max_length=20,default='<Reviewer>',null=True)
   img = models.ImageField(upload_to='uploads/%Y/%m/%d/',height_field=None,width_field=None,max_length=100)
   def __str__(self):
      return str(self.reviewphotoid)

@python_2_unicode_compatible
class Feature(models.Model):
   featureid = models.AutoField(primary_key=True)
   name = models.CharField(max_length=20,default='<Item>',null=True)
   def __str__(self):
      return str(self.name)
   class Meta:
      ordering = ( 'name', )

@python_2_unicode_compatible
class ReviewFeature(models.Model):
   reviewfeatureid = models.AutoField(primary_key=True)
   reviewid = models.ForeignKey(Review,on_delete=models.CASCADE)
   featureid = models.ForeignKey(Feature, on_delete=models.CASCADE)
   rating = models.DecimalField(null=True,max_digits=3,decimal_places=1)
   def __str__(self):
      return str(self.reviewfeatureid)
   class Meta: 
      ordering = ( 'featureid__name', )

@python_2_unicode_compatible
class Journal(models.Model):
   journalid = models.AutoField(primary_key=True)
   enteredby = models.ForeignKey(Reviewer,null=True,on_delete=models.CASCADE)
   entrydate = models.DateTimeField('Date',default=timezone.now)
   textdata = models.TextField(null=True)
   def __str__(self):
     return str(self.entrydate)
   class Meta:
     ordering = ( '-entrydate', )

@python_2_unicode_compatible
class JournalPhoto(models.Model):
   journalphotoid = models.AutoField(primary_key=True)
   journalid = models.ForeignKey(Journal,on_delete=models.CASCADE)
   description = models.CharField(max_length=20,default='<Brief Description>',null=True)
   img = models.ImageField(upload_to='uploads/%Y/%m/%d/',height_field=None,width_field=None,max_length=100)
   def __str__(self):
      return str(self.journalphotoid)

@python_2_unicode_compatible
class Tag(models.Model):
   tagid = models.AutoField(primary_key=True)
   name = models.CharField(max_length=20,default='<Item>',null=True)
   def __str__(self):
      return str(self.name)
   class Meta:
      ordering = ( 'name', )

@python_2_unicode_compatible
class JournalTag(models.Model):
   journaltagid = models.AutoField(primary_key=True)
   journalid = models.ForeignKey(Journal,on_delete=models.CASCADE)
   tagid = models.ForeignKey(Tag, on_delete=models.CASCADE)
   def __str__(self):
      return str(self.journaltagid)
   class Meta:
      ordering = ( 'journalid__entrydate', )

