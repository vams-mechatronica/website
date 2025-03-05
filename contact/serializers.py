from rest_framework import serializers
from .models import ContactUsForm, SubscribedToNewsletter

class ContactUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsForm
        fields = '__all__'

class SubscribedToNewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribedToNewsletter
        fields = '__all__'