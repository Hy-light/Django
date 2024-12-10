from rest_framework import serializers
from watchlist_app.models import Movie

# Model.Serializers
class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"         # allows for all fields to be serialized or deserialized
        # fields = ('name', 'description', 'active')  # allows for only specific fields to be serialized or deserialized.
        # exclude = ('id',)  # excludes a desired field from the serialized output.
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and description should not be the same.')
        return data
    
    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Name should be at least 5 characters long.')
        return value
