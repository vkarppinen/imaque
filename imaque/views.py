import logging
import os
import sys
from base64 import b64encode

import cloudinary
import cloudinary.uploader
from pyramid.response import Response
from pyramid.view import view_config

logging.basicConfig(
    format='[%(asctime)-15s}8s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


if 'CLOUDINARY_CLOUD_NAME' in os.environ and \
   'CLOUDINARY_API_KEY' in os.environ and \
   'CLOUDINARY_API_SECRET' in os.environ:

    config = cloudinary.config(
        cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
        api_key=os.environ.get('CLOUDINARY_API_KEY'),
        api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
    )

else:
    logger.error('Environment variables not set. Exiting...')
    sys.exit(0)



@view_config(route_name='form', renderer='templates/template.jinja2')
def form(request):
    return dict()


def handle_delete(request):
    try:
        image_id = request.POST['image_id']
    except Exception as e:
        logger.error(e)
        return Response('An error occurred. Image could not be deleted.')

    result = cloudinary.uploader.destroy(image_id)
    return Response(json=result)


def handle_upload(request):
    try:
        image = request.POST['image']
        b64data = b64encode(image.file.read())
        mimetype = image.type

        # handle image tags
        if 'tags' in request.POST:
            tags = request.POST['tags']
        else:
            tags = []
    except Exception as e:
        logger.error(e)
        return Response('An error occurred. No image was sent!')

    # handle incorrect file types.
    if image.type not in ['image/jpeg', 'image/jpg', 'image/png']:
        return Response(f'Image file type ({0}) not supported.'
                        .format(image.type))

    # handle file size
    if request.content_length > 2000000:
        return Response(f'Only under 2mb images supported.')

    data_uri = 'data:{0};base64,{1}'.format(mimetype, b64data.decode('utf-8'))
    result = cloudinary.uploader.upload(data_uri, tags=tags)
    return Response(json=result)