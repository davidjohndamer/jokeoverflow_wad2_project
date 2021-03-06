"""jokeoverflow_wad2_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from jokeoverflow import views

app_name = 'jokeoverflow'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^about_us/', views.about_us, name='about_us'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^latest_news/', views.latest_news, name='latest_news'),
    url(r'^user_profiles/', views.user_profiles, name='user_profiles'),
    url(r'^top_rated_videos/', views.top_rated_videos, name='top_rated_videos'),
    url(r'^top_rated_jokes/', views.top_rated_jokes, name='top_rated_jokes'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),

]
