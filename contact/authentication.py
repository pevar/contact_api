__author__ = 'cbartolini'

from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class FakeAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('X_USERNAME')
        password = request.META.get('X_PASSWORD')
        if not (username and password):
            return None

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return user, None
