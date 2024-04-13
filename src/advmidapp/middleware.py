from django.http import JsonResponse
import json

def check_even(get_response):
    print("check_even middleware")
    def wrapper(request):
        print('start of check_even')
        print(f"post data={request.body}")
        try:
            data=json.loads(request.body)
            number=data.get('number')
            if number and (number) % 2:
                return JsonResponse({"message":"Failed from the middleware"})
        except json.JSONDecodeError:
            return JsonResponse({"message":"invalid json data format"})
        response=get_response('request')
        print("end of check_even")
        return response
    return wrapper