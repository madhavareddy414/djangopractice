from django.http import HttpResponse

class HttpResponseMixins(object):
    def render_to_HttpRespnose(self,json_data):
        return HttpResponse(json_data,content_type='application/json')