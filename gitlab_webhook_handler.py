import json
from StringIO import StringIO


def process_gitlab_data(request):
    data = request.json
    return json.dumps(data)
