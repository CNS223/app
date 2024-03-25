from django.http import JsonResponse

def store_in_session(request, key, value):
	request.session[key] = value
	request.session.save()
	request.session.modified = True
	return JsonResponse({'message': f'Key "{key}" stored successfully'}, status=200)