from rest_framework import authentication


class AuthenticationProvider(authentication.BaseAuthentication):
    def authenticate(self, request):
        return None

        # print(request)
        #
        #
        # # TODO: authentication gets the authorization code
        # # Check in database if user exists, if user doesn't exist, create session
        # return None