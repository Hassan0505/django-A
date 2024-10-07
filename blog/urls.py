from django.urls import path
from. import views
urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about' ),
    path('green/', views.Green.as_view(), name='green'),
]