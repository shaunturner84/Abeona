from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Home Page
    url(r'^$', views.index, name='index'),

    # Order by date
    url(r'^order-by-date$', views.order_by_date, name='order by date'),

    # Review Page
    url(r'^review-(?P<review_id>[0-9]+)$', views.review, name='review'),

    # Journal Page
    url(r'^journal-(?P<journal_id>[0-9]+)$', views.journal, name='journal'),


    # journals by date
    url(r'^journals-by-date$', views.journals_by_date, name='journals by date'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
