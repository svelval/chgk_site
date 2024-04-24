from quart import url_for


def static_files_context_processor(*path, blueprint='', **kwargs):
    return url_for(endpoint=f'{blueprint}.static', filename='/'.join(path), **kwargs)
