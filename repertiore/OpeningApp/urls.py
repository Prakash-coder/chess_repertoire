from django.urls import path
from .views import OpeningList, OpeningDetail

urlpatterns = [
    path('', OpeningList.as_view(), name='opening-list'),
    path('openings/', OpeningList.as_view(), name='opening-list'),
    path('openings/<int:pk>/', OpeningDetail.as_view(), name='opening-detail'),
]
