from rest_framework import authentication


class AuthenticationProvider(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(request)

        # TODO: make request with access token, and get the user details
        # Check in database if user exists, if user doesn't exist, create session
        return None