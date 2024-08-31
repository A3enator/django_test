from django.urls import path
from .views import home_view, aboutme_view, Homepage_view, Aboutpage_view

urlpatterns = [
    # path("", home_view, name="home"),
    # path("about/", aboutme_view, name="about me"),
    path("", Homepage_view.as_view(), name="home"),
    path("class/about", Aboutpage_view.as_view(), name="about"),
]
