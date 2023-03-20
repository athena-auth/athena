from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class AuthenticationManager(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(request.data)
        pass
