from django.urls import path
from .views import *

urlpatterns = [
    path('qualififcation_status/<int:user_pk>', UserQualificationAPI.as_view()),
    path('passport/<int:user_pk>', UserPassportAPI.as_view()),
    path('passport_scans/<int:user_pk>', UserScansApi.as_view()),
    path('rules/<int:user_pk>', UserRulestAPI.as_view()),
]