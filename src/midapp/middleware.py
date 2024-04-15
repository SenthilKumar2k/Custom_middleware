"""Django middleware function named set_request_data that modifies the incoming HTTP request before 
passing it to the next middleware or view in the Django request-response cycle."""


# def set_request_data(get_response):
#     print('set_request_data middleware')
#     def wrapper(request):
#         print(f'post data={request.POST}')
#         data=request.POST.get('number')
#         request.POST={'data':data}
#         print('start of set_request_data')
#         response=get_response(request)
#         print('end of set_request_data')
#         return response
#     return wrapper

"""request data"""
#form-data -> key=number, value=2 

"""output"""
# post data=<QueryDict: {'number': ['2']}>
# start of set_request_data
# index call {'data': '2'}
# end of set_request_data


# Middleware Function Structure:

"""set_request_data is a middleware function that takes get_response as a parameter. 
In Django, middleware functions are callable objects that can modify request or response 
objects, typically by wrapping other views or middleware in a chain."""

# Inner Wrapper Function (wrapper):

"""Inside set_request_data, a nested function wrapper is defined. 
This function will replace the default behavior of handling a request."""

# Middleware Logic:

"""The get_response function is called with the modified request object. This get_response function 
represents the next middleware in the chain or the actual view that will process the request."""

#Returning Response:(return response)

"""The modified response (possibly altered by other middleware or the view) is returned back up the 
middleware chain to the client."""

#(return wrapper)

"""Finally, the wrapper function is returned. This returned function will be used to handle the 
incoming requests. When Django processes a request, it will pass the request through this middleware, 
which can modify the request before passing it further along the chain."""

import json

def set_request_data(get_response):
    print('set_request_data_midleware')
    def wrapper(request):
        print(f"post data={request.body}")
        try:
            data=json.loads(request.body)
            number=data.get('number')
            request.custom_data={"data":number}
            print("start of set_request_data")
        except json.JSONDecodeError:
            print("json data is in invalid format")
        response=get_response(request)
        print("end of set request data")
        return response
    return wrapper