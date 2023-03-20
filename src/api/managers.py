from rest_framework import authentication


class AuthenticationManager(authentication.BaseAuthentication):
    def authenticate(self, request):
        return None