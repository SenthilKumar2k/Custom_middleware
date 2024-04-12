"""Django middleware function named set_request_data that modifies the incoming HTTP request before 
passing it to the next middleware or view in the Django request-response cycle."""


def set_request_data(get_response):
    print('set_request_data middleware')
    def wrapper(request):
        print(f'post data={request.POST}')
        data=request.POST.get('number')
        request.POST={'data':data}
        print('start of set_request_data')
        response=get_response(request)
        print('end of set_request_data')
        return response
    return wrapper


"""output"""
# post data=<QueryDict: {'number': ['2']}>
# start of set_request_data
# index call {'data': '2'}
# end of set_request_data

# step 1

