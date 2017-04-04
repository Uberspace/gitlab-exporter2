import os
from bottle import route, run, request, abort
from prometheus_metrics import get_prometheus_metrics
from gitlab_webhook_handler import process_gitlab_data


def check_secret(request):
    token = request.headers.get('X-Gitlab-Token')
    if token == secret:
        return True
    else:
        abort(401, "Access denied.")


@route('/metrics', 'GET')
def metrics():
    return get_prometheus_metrics()


@route('/gitlab', 'POST')
def gitlab():
    check_secret(request)
    return process_gitlab_data(request)


host = os.environ.get('HOST', '::')
port = os.environ.get('PORT', 8080)
secret = os.environ.get('SECRET', '')

run(host=host, port=port)
