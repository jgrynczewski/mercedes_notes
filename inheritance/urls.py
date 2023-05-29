from django.urls import path

from inheritance import views

urlpatterns = [
    path('1/', views.first_view),
    path('2/', views.second_view),
]