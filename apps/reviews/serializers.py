from rest_framework import serializers

from apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = 'renter'

    def validate(self, data):
        user = self.context['request'].user
        booking = data.get('booking')

        if booking.renter != user:
            raise serializers.ValidationError(
                'You cannot review this reservation cause you are not an owner'
            )

        return data

