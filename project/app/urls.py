from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('image/<int:image_id>/',views.image_detail, name='image_detail'),
    path('search/', views.search, name='search'),
]