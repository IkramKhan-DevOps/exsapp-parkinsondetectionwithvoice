from rest_framework import serializers
from src.accounts.models import User
from src.api.models import Predication


class UserPasswordChangeSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk', 'profile_image', 'first_name', 'last_name', 'username',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk', 'profile_image', 'first_name', 'last_name', 'username', 'email', 'phone_number'
        ]
        read_only_fields = [
            'email', 'date_joined'
        ]


""" CAPTURES """


class PredicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predication
        read_only_fields = [
            'is_active', 'mdvp_fo', 'mdvp_fhi',
            'mdvp_flo', 'mdvp_shimmer',
            'mdvp_jitter', 'rpde', 'd2', 'nhr', 'hnr', 'dfa',
            'ppe', 'ppe', 'spread1', 'spread2', 'status'
        ]
        exclude = ['user']
