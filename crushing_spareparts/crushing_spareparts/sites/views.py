from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Site
from .serializers import SiteSerializer
from rest_framework.generics import get_object_or_404
#from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class SiteViewSet(viewsets.ViewSet):
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        site = Site.objects.all()
        serializer = SiteSerializer(site, many=True, context={"request":request})
        response_dict = {"error": False, "message": "List of all Sites", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer=SiteSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Site saved successfully"}
        except:
            dict_response={'error': True, 'message':"Error During Saving Site"}
        return Response(dict_response)

    def update(self, request):
        try:
            queryset = Site.objects.all()
            site=get_object_or_404(queryset, pk=pk)
            serializer=SiteSerializer(site, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Successfully Updated Site"}
        except:
            dict_response={'error': True, 'message':"Error During Updating Site"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = Site.objects.all()
        site=get_object_or_404(queryset, pk=pk)
        serializer=SiteSerializer(site, context={"request": request})
        return Response({'error': False, 'message':"Single Data Fetch", "data": serializer.data})

    def destroy(self, request, pk=None):
        pass