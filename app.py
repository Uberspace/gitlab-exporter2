from bottle import route, run, request
from prometheus_metrics import get_prometheus_metrics
from gitlab_webhook_handler import process_gitlab_data


@route('/metrics', 'GET')
def metrics():
    return get_prometheus_metrics()


@route('/gitlab', 'POST')
def gitlab():
    return process_gitlab_data(request)


run(host='::', port=8080)
