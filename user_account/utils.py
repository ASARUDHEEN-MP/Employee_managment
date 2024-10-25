# utils.py

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
