from rest_framework import serializers
from .models import * 


class QualificationSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Qualification 
        exclude = ['user']


class PassportSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Passport 
        exclude = ['scan_photo', 'scan_registration', 'user']


class UserScansSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Passport 
        fields = ['scan_photo', 'scan_registration']
        extra_kwargs = {
                        'scan_photo': {'required': True},
                        'scan_registration': {'required': True},
                        } 


class RulesSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Rules 
        exclude = ['user']