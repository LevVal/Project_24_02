import datetime
from urllib import request
from django.http import HttpResponse, HttpRequest
import json


def set_useragent_request_middleware(get_response):
    print("initial call")

    def middleware(request: HttpRequest):
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        return response

    return middleware


class ThrottlingMiddleware:
    #{"127.0.0.1": [0, 0, 0]}
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):

        with open('user_ip.json', 'r') as last_ip_file:
            data = json.load(last_ip_file)

            for ip, time in data.items():
                last_ip = ip

                last_time = datetime.timedelta(
                    hours=time[0],
                    minutes=time[1],
                    seconds=time[2],
                    microseconds=time[3]
                )

            user_ip = request.META['REMOTE_ADDR']
            user_time = datetime.datetime.now().time()

            with open('user_ip.json', 'w') as last_ip_file:
                data[user_ip] = [user_time.hour,
                                 user_time.minute,
                                 user_time.second,
                                 user_time.microsecond]
                last_ip_file.write(json.dumps(data))

                user_time = datetime.timedelta(
                    hours=user_time.hour,
                    minutes=user_time.minute,
                    seconds=user_time.second,
                    microseconds=user_time.microsecond
                )

            check_time = (user_time - last_time)
            if user_ip == last_ip and check_time < datetime.timedelta(seconds=10):
                raise Exception("Do not send more than 10 seconds")

        response = self.get_response(request)
        return response

class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0


    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print("request: ", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("response: ", self.responses_count)
        # self.exceptions_count += 1
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print("exception: ", self.exceptions_count)


