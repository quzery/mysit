from django.conf.urls import url, include
import login.views

urlpatterns = [
    url(r'^$', login.views.auth_login),
    url(r'^home', login.views.home),
]