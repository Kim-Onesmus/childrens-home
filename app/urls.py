from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.Login, name='login'),
    path('account/<str:pk>/', views.Accountdetails, name='account'),
    path('lacation', views.Location, name='location'),
    path('ask_question/<str:pk>/', views.Ask_question, name='ask_question'),
    path('book_visit', views.bookVisit, name='book_visit'),
    path('thanks', views.Thanks, name='thanks'),
    path('contact', views.Contact, name='contact'),
    path('donate', views.Donate, name='donate'),
    path('logout', views.Logout, name='logout'),
]