import os

def hubpath_processor(request):
    return {'jupyterhub_path': os.environ.get('JUPYTERHUB_PATH', '/notebook/')}