from django.core.serializers import serialize
import json

class MixinSerialize(object):
    def serialize1(self,qs):
        jsone_data =serialize('json',qs)
        p_data_json = json.loads(jsone_data)
        final_list = []
        for obj in p_data_json:
            emp_data= obj['fields']
            final_list.append(emp_data)
        jsone_data= json.dumps(final_list)
        return jsone_data

from django.http import HttpResponse

class HttpResponseMixin(object):
    def render_to_http_respnose(self,json_data, status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)