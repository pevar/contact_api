from django.db import models
from django.utils.text import ugettext_lazy as _


class Contact(models.Model):
    first_name = models.CharField(_('First Name'), max_length=250)

    def __str__(self):
        return self.first_name
