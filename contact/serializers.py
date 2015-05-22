__author__ = 'cbartolini'

from contact.models import Contact

from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', )
