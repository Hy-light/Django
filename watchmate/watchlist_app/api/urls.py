from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')



urlpatterns = [
    # Add your URL patterns here.
    path('list/', WatchListAV.as_view(), name='movie-list' ),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail' ),  # Add this line to create a detail view for each movie.
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'), # Add this line to create a detail view for each
    
    # path('review/', ReviewList.as_view(), name='review-list'),  # Add this line to create a review view for each movie.)
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),  # Add this line to create a detail view for each review.
    
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),  # Add this line to include review URLs for each movie.
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),  # Add this line to include a create view for each review.
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),  # Add this line to include a detail view for each review.
]