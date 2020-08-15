from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os

class OverwriteStorage(FileSystemStorage):
    '''
    If the file exists, then remove it before storage it.

    thanks for https://gist.github.com/fabiomontefuscolo/1584462.
    '''
    def get_available_name(self, name, max_length):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return super(OverwriteStorage, self).get_available_name(name, max_length)
