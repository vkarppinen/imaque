from pyramid.config import Configurator
from imaque.views import handle_upload, handle_delete


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('form', '/')

    config.add_route('upload', '/upload', request_method='POST')
    config.add_view(handle_upload, route_name='upload')

    config.add_route('delete', '/delete', request_method='POST')
    config.add_view(handle_delete, route_name='delete')

    config.scan()
    return config.make_wsgi_app()
