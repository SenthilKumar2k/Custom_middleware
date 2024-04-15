from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    print('index call', request.custom_data)
    return JsonResponse({'message':'set data received successfully'})

# You import csrf_exempt decorator from django.views.decorators.
# csrf to exempt this view from CSRF protection.
