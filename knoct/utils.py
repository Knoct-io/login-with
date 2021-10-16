import os
import uuid

from box import Box


def upload_to_random(base, filename):
  _, ext = os.path.splitext(filename)

  if not base.endswith('/'):
    base += '/'

  return f'{base}{uuid.uuid4()}{ext}'


def image_upload_to_random(instance, filename):
  return upload_to_random('images', filename)


def templatable_form_errors(form):
  """
  Returns first error message for each field in form.
  """
  error_map = {
    key: form.errors.get(key, [None])
    for key in form.fields.keys()
  }

  return Box({
    key: error
    for key, (error, *_) in error_map.items()
  })
