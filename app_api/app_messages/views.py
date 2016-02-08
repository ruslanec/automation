from django.shortcuts import render
from rest_framework import viewsets

#import sys
#sys.path.insert(0, '../')

from app_messages.models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

