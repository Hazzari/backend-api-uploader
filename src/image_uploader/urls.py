from django.urls import path

from . import views
app_name = 'authentication'

urlpatterns = [
    path('', views.ImageViewSet.as_view()),
]
