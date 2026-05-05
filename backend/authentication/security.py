import os
from dataclasses import dataclass
from rest_framework import authentication, exceptions


@dataclass
class ServiceUser:
    username: str = 'bonevibauth-service'
    is_authenticated: bool = True


class BearerTokenAuthentication(authentication.BaseAuthentication):
    """轻量 Bearer Token 验证，呼应作品书中的 bearer authorization。"""

    def authenticate(self, request):
        expected_token = os.getenv('BVA_API_TOKEN', '')
        if not expected_token:
            return None

        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            raise exceptions.AuthenticationFailed('Missing bearer token')

        token = auth_header.removeprefix('Bearer ').strip()
        if token != expected_token:
            raise exceptions.AuthenticationFailed('Invalid bearer token')

        return ServiceUser(), None
