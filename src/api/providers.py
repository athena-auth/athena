from rest_framework import authentication


class AuthenticationProvider(authentication.BaseAuthentication):
    def authenticate(self, request):
        return None