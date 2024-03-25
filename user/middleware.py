import jwt
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from user.models import UserSystemVisit

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

class VisitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'session_counter' in request.session:
            request.session['session_counter'] += 1
        else:
            request.session['session_counter'] = 1
        self.update_visit_count(request)

        response = self.get_response(request)
        # Process response
        return response

    def update_visit_count(self, request):
        today = timezone.now().date()
        visit, created = UserSystemVisit.objects.get_or_create(created_at=today)
        if not created:
            visit.daily_count += 1
            visit.total_count = UserSystemVisit.objects.last().total_count+1
            visit.save()
        # print("daily_count", visit.daily_count)
        # print("total_count", visit.total_count)