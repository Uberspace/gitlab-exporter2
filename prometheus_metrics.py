from prometheus_client import Summary, generate_latest


REQUEST_TIME = Summary(
    'request_processing_seconds',
    'Time spent processing request'
)


@REQUEST_TIME.time()
def process_request():
    return generate_latest()


def get_prometheus_metrics():
    return process_request()
