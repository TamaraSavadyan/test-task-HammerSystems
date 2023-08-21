from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import PhoneAuthSerializer, VerificationSerializer
import random
import time

class AuthView(APIView):
    def post(self, request):
        serializer = PhoneAuthSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = str(random.randint(1000, 9999))

            time.sleep(3)

            request.session['phone_number'] = phone_number
            request.session['verification_code'] = verification_code

            return Response({'message': 'Verification code sent'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerificationView(APIView):
    def post(self, request):
        serializer = VerificationSerializer(data=request.data)
        if serializer.is_valid():
            user_entered_code = serializer.validated_data['verification_code']
            stored_code = request.session.get('verification_code')

            if user_entered_code == stored_code:
                # Verification successful
                return Response({'message': 'Verification successful'}, status=status.HTTP_200_OK)
            else:
                # Verification failed
                return Response({'message': 'Verification failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
