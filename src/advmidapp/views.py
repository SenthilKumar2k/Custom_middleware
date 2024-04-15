from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def check_index(request):
    print("Check index call", request.custom_data)
    return JsonResponse({"message":"data checked and received succesfully"})
