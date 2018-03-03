from base64 import b64encode

from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='form', renderer='templates/template.jinja2')
def form(request):
    return dict()


def handle_upload(request):
    try:
        image = request.POST['image']
        b64image = b64encode(image.file.read())
    except:
        return Response('No image was sent!')

    return Response(
        'not implemented yet'
    )