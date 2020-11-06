from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

import os

from .serializers import *
from .models import *


class UserQualificationAPI(APIView): 
    def get(self, request, user_pk): 
        user = User.objects.get(pk=user_pk)
        
        try:
            qualification = user.qualification
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = QualificationSerializer(qualification) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        serializer = QualificationSerializer(data=request.data)
        if serializer.is_valid():
            passport = serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPassportAPI(APIView): 
    def post(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        serializer = PassportSerializer(data=request.data)
        if serializer.is_valid():
            passport = serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserScansApi(APIView):
    def put(self, request, user_pk): 
        user = User.objects.get(pk=user_pk)

        try:
            passport = user.passport
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserScansSerializer(data=request.FILES)
        if serializer.is_valid():
            if passport.scan_photo or passport.scan_registration:
                if os.path.exists(passport.scan_photo.path):
                    os.remove(passport.scan_photo.path)

                if os.path.exists(passport.scan_registration.path):
                    os.remove(passport.scan_registration.path)

            passport.scan_photo = serializer.validated_data['scan_photo']
            passport.scan_registration = serializer.validated_data['scan_registration']
            passport.save()

            return Response(status=status.HTTP_204_NO_CONTENT) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRulestAPI(APIView): 
    def post(self, request, user_pk):
        user = User.objects.get(pk=user_pk)
        serializer = RulesSerializer(data=request.data)
        if serializer.is_valid():
            rules = serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




