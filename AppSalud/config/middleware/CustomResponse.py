from django.http import HttpResponse
from ..Utils.create_response import create_response
import json

class CustomResponseMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        parseResponse,code = create_response(response.status_code,"Ok",json.loads(response.getvalue()))
        return HttpResponse(json.dumps(parseResponse),content_type="application/json",status=code)

    def process_exception(self,request, exception):
        print("Exception")