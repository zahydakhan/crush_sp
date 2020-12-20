from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import SitesPurchaseRequest, MainPurchaseRequest
from .serializers import SitePRSerializer, MainPRSerializer
from rest_framework.generics import get_object_or_404
#from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class SitesPRViewSet(viewsets.ViewSet):
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        site = SitesPurchaseRequest.objects.all()
        serializer = SitePRSerializer(site, many=True, context={"request":request})
        response_dict = {"error": False, "message": "List of all purchase requests", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer=SitePRSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Purchase request saved successfully"}
        except:
            dict_response={'error': True, 'message':"Error During Saving Purchase Request"}
        return Response(dict_response)

    def update(self, request):
        try:
            queryset = SitesPurchaseRequest.objects.all()
            site=get_object_or_404(queryset, pk=pk)
            serializer=SitePRSerializer(site, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Successfully Updated Purchase Request"}
        except:
            dict_response={'error': True, 'message':"Error During Updating Purchase Request"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = SitesPurchaseRequest.objects.all()
        site=get_object_or_404(queryset, pk=pk)
        serializer=SitePRSerializer(site, context={"request": request})
        return Response({'error': False, 'message':"Single Data Fetch", "data": serializer.data})

    def destroy(self, request, pk=None):
        pass



class MainPRViewSet(viewsets.ViewSet):
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        site = MainPurchaseRequest.objects.all()
        serializer = MainPRSerializer(site, many=True, context={"request":request})
        response_dict = {"error": False, "message": "List of Main Purchase Requests", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer=MainPRSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Main purchase request saved successfully"}
        except:
            dict_response={'error': True, 'message':"Error During Saving Main Purchase Request"}
        return Response(dict_response)

    def update(self, request):
        try:
            queryset = MainPurchaseRequest.objects.all()
            site=get_object_or_404(queryset, pk=pk)
            serializer=MainPRSerializer(site, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Successfully Updated Main Purchase Request"}
        except:
            dict_response={'error': True, 'message':"Error During Updating Main Purchase Request"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = MainPurchaseRequest.objects.all()
        site=get_object_or_404(queryset, pk=pk)
        serializer=MainPRSerializer(site, context={"request": request})
        return Response({'error': False, 'message':"Single Data Fetch", "data": serializer.data})

    def destroy(self, request, pk=None):
        pass