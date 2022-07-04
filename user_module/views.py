from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import (RegistrationSerializer,
                          UserLoginSerializer,
                          ForgotPasswordSerializer,
                          ResetPasswordSerializer,
                          LogoutSerializer)


class Registration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serialized_data = self.serializer_class(data=request.data)
        valid = serialized_data.is_valid(raise_exception=True)

        if valid:
            serialized_data.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered! Please check mail for credentials!',
                'user': serialized_data.data,
            }

            return Response(response, status=status_code)
        else:
            return Response(serialized_data.errors, status.HTTP_400_BAD_REQUEST)


class UserLogin(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ForgotPassword(generics.GenericAPIView):
    def post(self, request):
        serializers = ForgotPasswordSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            return Response({'message': 'Check email for password reset link!'}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# View class for resetting password using link received
class ResetPassword(generics.GenericAPIView):
    def post(self, request, uid, token):
        serializers = ResetPasswordSerializer(data=request.data, context={
            'uid': uid, 'token': token})
        if serializers.is_valid(raise_exception=True):
            return Response({'message': 'Password reset successful!'}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# View class for blacklisting refresh token on User Logout
class Logout(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response({'message': 'Logout Successful!'}, status=status.HTTP_200_OK)
