from django.urls import path
from .import views
urlpatterns = [
     path('',views.index,name="home"),
     path('courses/',views.course,name='courses'),
     path('faculty/',views.faculty,name='faculty'),
     path('contact/',views.contact,name='contact'),
     path('new/',views.new,name='new')]