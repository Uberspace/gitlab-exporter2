from prometheus_client import Summary, generate_latest
import random
import time


REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


def get_prometheus_metrics():
    process_request(random.random())
    return generate_latest()
