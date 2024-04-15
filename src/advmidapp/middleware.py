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
            request.custom_data={'data':number}
            if number and int(number) % 2:
                return JsonResponse({"message":"Failed from the middleware"})
        except json.JSONDecodeError:
            return JsonResponse({"message":"invalid json data format"})
        response=get_response(request)
        print("end of check_even")
        return response
    return wrapper

"""input"""
#raw json {"number":2}

"""output"""
# start of check_even
# post data=b'{\n"number":2\n}'
# Check index call {'data': 2}
# end of check_even



# def check_even(get_response):
#     print('check_even middleware')

#     def wrapper(request):
#         print('Start of check_even')
#         number = request.POST.get('number')
#         is_odd = False
#         if number and int(number) % 2:
#             return JsonResponse({"message": "Failed from the middleware",})
#         response = get_response(request)
#         print('End of check_even')
#         return response
#     return wrapper

"""request data"""
#form-data -> key=number, value=2 
