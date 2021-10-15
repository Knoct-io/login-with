import os
import uuid


def upload_to_random(base, filename):
  _, ext = os.path.splitext(filename)

  if not base.endswith('/'):
    base += '/'

  return f'{base}{uuid.uuid4()}{ext}'


def image_upload_to_random(instance, filename):
  return upload_to_random('images', filename)
