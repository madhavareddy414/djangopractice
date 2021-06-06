
class SampleMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('hitting custome')

    def __call__(self,request, *args, **kwargs):

       resp = self.get_response(request)
       return resp


