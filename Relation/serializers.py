from rest_framework import serializers
from .models import Relation

class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = ['id', 'follower', 'following']
        read_only_fields = ['follower']

    def validate(self, data):
        if data['following'] == self.context['request'].user:
            raise serializers.ValidationError("You cannot follow yourself.")
        return data