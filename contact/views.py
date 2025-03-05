from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import ContactUsForm, SubscribedToNewsletter
from .serializers import ContactUsFormSerializer, SubscribedToNewsletterSerializer
# Create your views here.
# ViewSet
class ContactUsFormViewSet(viewsets.ModelViewSet):
    queryset = ContactUsForm.objects.all()
    serializer_class = ContactUsFormSerializer
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_messages = ContactUsForm.objects.order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_messages, many=True)
        return Response(serializer.data)

class SubscribedToNewsletterView(generics.ListCreateAPIView):
    queryset = SubscribedToNewsletter.objects.all()
    serializer_class = SubscribedToNewsletterSerializer

