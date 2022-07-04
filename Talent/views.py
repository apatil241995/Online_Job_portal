from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import serializer
from . import models


class TalentDetailsApi(generics.CreateAPIView):
    serializer_class = serializer.TalentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.role != "TALENT":
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            # print("REQUEST DATA", request.data)
            user_details = models.TalentDetails.objects.filter(email_id=user.id).exists()
            # serialized_data = serializer.CompanySerializer(user_details)
            print(user_details)
            if user_details:
                response = {
                    'success': False,
                    'status_code': status.HTTP_403_FORBIDDEN,
                    'message': 'Talent details already exist'
                }
                return Response(response, status.HTTP_403_FORBIDDEN)
            else:
                serializer = self.serializer_class(data=request.data)
                valid = serializer.is_valid(raise_exception=True)

                if valid:
                    serializer.save()
                    status_code = status.HTTP_201_CREATED

                    response = {
                        'success': True,
                        'statusCode': status_code,
                        'message': 'Employee successfully registered! Please check mail for credentials!',
                        'user': serializer.data,
                    }

                    return Response(response, status=status_code)
                else:
                    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
