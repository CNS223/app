import jwt
from django.conf import settings
from django.http import JsonResponse

class TokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = request.session.get('access_token')
        if access_token:
            try:
                decoded_token = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
                # Perform additional token validation checks here if needed
                request.user_id = decoded_token.get('user_id')
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Access token has expired'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'error': 'Invalid access token'}, status=401)

        response = self.get_response(request)
        return response