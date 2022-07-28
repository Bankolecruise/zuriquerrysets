from django.utils import timezone
from . import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .models import Link
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from . import models

from rest_framework import status

from .serializers import LinkSerializer


class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    

class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self,request):
        """
        Invoked whenever a HTTP GET Request is made tot this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, staus=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently crreated active links
    """
    def get(self, request):
        """
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerialzer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    

    
    

# Create your views here.
