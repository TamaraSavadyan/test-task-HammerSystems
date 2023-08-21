from rest_framework import serializers

class PhoneAuthSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)

class VerificationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)
