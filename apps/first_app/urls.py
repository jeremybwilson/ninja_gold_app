from django.conf.urls import url
from . import views           # This line is new!

app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.index, name="index"),  # This line has changed!
    url(r'^reset$', views.reset, name="reset"),
    url(r'^process/$', views.process, name="process")
]