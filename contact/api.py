__author__ = 'cbartolini'

from contact.models import Contact
from rest_framework import viewsets
from contact.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer