from django.http import HttpResponse
# from rest_framework.renderers import JSONRenderer
import json


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data_dict, **kwargs):
        # content = JSONRenderer().render(data)
        content = json.dumps(data_dict)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)