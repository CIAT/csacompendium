from django.conf.urls import url
from .views import (
    LocationCreateAPIView,
    LocationDeleteAPIView,
    LocationDetailAPIView,
    LocationListAPIView,
)

urlpatterns = [
    url(r'^$', LocationListAPIView.as_view(), name='list'),
    url(r'^create/$', LocationCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', LocationDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/delete/$', LocationDeleteAPIView.as_view(), name='delete'),
]
