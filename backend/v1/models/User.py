from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from backend.private import SECRET_KEY
from django.core.exceptions import ValidationError

import re

from units import Upload_Byhash


class User(models.Model):
    """
    The model about users. Remember, this models will hash the pass auto
    """
    name = models.CharField(max_length=100, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=600, blank=False)
    headpic = models.ImageField(upload_to=Upload_Byhash.to_img('headpic'), blank=True)

    def __str__(self):
        return f"{self.name}"

    def clean(self, *args, **kwargs):
        # password: length >= 6
        # name: like '(\+\s)\s+'
        if len(self.password) < 6:
            raise ValidationError({'password': 'Password is too short (< 6), please re-enter.'})

        re_c = re.compile(r'^(\S+\s+)*\S+$')
        if not re_c.match(self.name):
            raise ValidationError({
                'name': [
                    f'Name {repr(self.name)} is not vaild, please let it only has the Chinese '
                    'characters or English characters and the space is only in two non-space '
                    'characters which has max length: 1.'
                ]
            })

    def save(self, *args, **kwargs):
        # Ensure all attr is vaild
        self.full_clean()

        # pre-deal with all data
        self.password = make_password(self.password + SECRET_KEY)
        return super().save(*args, **kwargs)

    def check_password(self, password):
        return check_password(password + SECRET_KEY, self.password)
