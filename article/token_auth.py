import  jwt
from articles.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import  AuthenticationFailed,APIException
from rest_framework import status


class ValidationErrorFailed(APIException):
    status_code = status.HTTP_200_OK
    def __init__(self, detail):
        self.detail = detail

class TokenAuth(BaseAuthentication):
    def authenticate(self, request):
        base_message = 'Wrong token'

        auth_token = request.META.get("HTTP_AUTHTOKEN","")
        if not auth_token:
            raise ValidationErrorFailed(base_message)

        try:
            payload = jwt.decode(auth_token,"SECRET_KEY",algorithm=('HS256'))
        except(jwt.InvalidTokenError,jwt.exceptions.DecodeError):
            raise ValidationErrorFailed(base_message)

        email = payload.get("email")
        if not email:
            raise ValidationErrorFailed(base_message)

        request.META['email'] = email


class ValidationErrorFailed(APIException):
    status_code = status.HTTP_200_OK
    def __init__(self, detail):
        self.detail = detail

def token_auth(token):
    payload = jwt.decode(token,"SECRET_KEY",algorithm="HS256")
    email=payload.get("email")
    user = User.objects.filter(email=email)
    if  not user:
        return  False
    return  True