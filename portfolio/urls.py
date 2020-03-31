from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='portfolio'),
    path('piece/<int:pk>', views.piece_detail, name='piece_detail'),
]
