from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dog/<slug:slug>', views.detail_page, name='detail_page' ),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('login/', views.loginuser, name='loginuser'),
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
]
