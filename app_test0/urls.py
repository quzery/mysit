from django.conf.urls import url, include
import app_test0.views

urlpatterns = [
    url(r'^$', app_test0.views.first_page),
    url(r'^all/', app_test0.views.all),
    url(r'^templay', app_test0.views.templay),
    url(r'^form/', app_test0.views.form),
    url(r'^investigate/', app_test0.views.investigate),
    url(r'^post_investigate/',app_test0.views.post_investigate),
]