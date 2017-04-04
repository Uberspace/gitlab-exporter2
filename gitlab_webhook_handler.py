from prometheus_client import Summary


pipeline_duration_seconds = Summary(
    'gitlab_pipeline_duration_seconds',
    'Time the pipeline took to run',
    ['project_name'])


def gitlab_to_prometheus(data):
    duration = data["object_attributes"]["duration"]
    project_name = data["project"]["name"]
    label = pipeline_duration_seconds.labels(project_name=project_name)
    label.observe(duration)


def process_gitlab_data(request):
    data = request.json
    gitlab_to_prometheus(data)
    return "Thank you"
