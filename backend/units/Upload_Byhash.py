from django.utils.deconstruct import deconstructible

from pathlib import Path
import hashlib
import os


def _base(dir_name: str, instance: 'Django obj', attr: str, filename: str) -> str:
    """
    The base function for all callable class-object: to_img  and so on ...

    Return the file path that need to upload like: {dir_name}/{hashcode}.{file's ext}
    """
    file_field = getattr(instance, attr)
    # with file_field.open() as file_:
    file_ = file_field.open()
    content = file_.read()
    assert type(content) == bytes
    hashcode = hashlib.sha256(content).hexdigest()

    _, ext = os.path.splitext(filename)

    return Path(dir_name) / hashcode[:2] / (hashcode[2:] + ext)


@deconstructible
class to_img(object):
    """
    The helper class to upload img resource. it need a string that the Image that you named in your
    models python file.

    return like: img/{hashcode}.{file's ext}
    """
    def __init__(self, attr: str):
        self.attr = attr

    def __call__(self, instance, filename):
        return _base('img', instance, self.attr, filename)
