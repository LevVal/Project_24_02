from django.http import HttpRequest
import datetime

def set_useragent_on_request_middleware(get_response):

    print("Initial call")

    def middleware(request: HttpRequest):
        print("Before get response")
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        print("After get response")
        return response

    return middleware

class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.response_count = 0
        self.exception_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print('requests_count: ', self.requests_count)
        response = self.get_response(request)
        if self.check_ip(request) == False:
            print('IP check failed. Not so fast.')
        self.response_count += 1
        print('response_count: ', self.response_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exception_count += 1
        print('exception_count: ', self.exception_count)

    def check_ip(self, request):
        print('remote;', request.META['REMOTE_ADDR'])

        #print(type(datetime.datetime.now()))

        #if self.time_out < datetime.timedelta(seconds=int(datetime.datetime.now().strftime("%S"))):
        return False

        ##if time_out > datetime.timedelta(minutes=1):
            #print('time out', datetime.timedelta(minutes=1))
        #print('get_ip: ', ip, datetime.datetime.now())
        #self.time = datetime.datetime.now()
        #if time_out < 10:
        #    raise PermissionDenied('time out'))

