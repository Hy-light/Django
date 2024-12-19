from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV,StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS, UserReview, WatchListGV


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')



urlpatterns = [
    # Add your URL patterns here.
    path('list/', WatchListAV.as_view(), name='movie-list' ),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail' ),  # Add this line to create a detail view for each movie.
    path('list2/', WatchListGV.as_view(), name='watch-list' ),
    
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'), # Add this line to create a detail view for each
    
    # path('review/', ReviewList.as_view(), name='review-list'),  # Add this line to create a review view for each movie.)
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),  # Add this line to create a detail view for each review.
    
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),  # Add this line to include review URLs for each movie.
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),  # Add this line to include a create view for each review.
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),  # Add this line to include a detail view for each review.
    path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),  # Add this line to include a user review view.
]