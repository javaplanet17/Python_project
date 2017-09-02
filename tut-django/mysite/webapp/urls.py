from django.conf.urls import url
from . import views

# Create your url pattern here.

urlpatterns = [
    url(r'^$',views.index, name='index')]
