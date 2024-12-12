from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)  # read_only=True for read-only field
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

# Model.Serializers
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # many=True for one-to-many relationship
    
    class Meta:
        model = WatchList
        fields = "__all__"         


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)  # many=True for one-to-many relationship
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"