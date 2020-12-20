from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import SparePart, Local_Comparison_SparePart, Roller
from .serializers import SparePartSerializer, LocalComparisonSparepartsSerializer, RollerSerializer
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class SparepartViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        spareparts = SparePart.objects.all()
        serializer = SparePartSerializer(spareparts, many=True, context={"request":request})
        response_dict = {"error": False, "message": "List of all Spareparts", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer=SparePartSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Sparepart saved successfully"}
        except:
            dict_response={'error': True, 'message':"Error During Saving Sparepart"}
        return Response(dict_response)

    def update(self, request):
        try:
            queryset = SparePart.objects.all()
            sparepart=get_object_or_404(queryset, pk=pk)
            serializer=SparePartSerializer(sparepart, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Successfully Updated Sparepart"}
        except:
            dict_response={'error': True, 'message':"Error During Updating Sparepart"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = SparePart.objects.all()
        sparepart=get_object_or_404(queryset, pk=pk)
        serializer=SparePartSerializer(sparepart, context={"request": request})
        return Response({'error': False, 'message':"Single Data Fetch", "data": serializer.data})

    def destroy(self, request, pk=None):
        pass

class SparePart_mn(generics.ListCreateAPIView):
    queryset = SparePart.MnLinerObjects.all()
    serializer_class = SparePartSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class SparePart_mp(generics.ListCreateAPIView):
    queryset = SparePart.MpObjects.all()
    serializer_class = SparePartSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class SparePart_get(generics.ListCreateAPIView):
    queryset = SparePart.GetObjects.all()
    serializer_class = SparePartSerializer
    #permission_classes = [IsAuthenticated]
    #authentication_classes = [JWTAuthentication]


class LocalComparisonSparepartViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        comparison_spareparts = Local_Comparison_SparePart.objects.all()
        serializer = LocalComparisonSparepartsSerializer(comparison_spareparts, many=True, context={"request":request})
        response_dict = {"error": False, "message": "List of all Local Spareparts", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer=LocalComparisonSparepartsSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Comparison sparepart saved successfully"}
        except:
            dict_response={'error': True, 'message':"Error During Saving Comparison Sparepart"}
        return Response(dict_response)

    def update(self, request):
        try:
            queryset = Local_Comparison_SparePart.objects.all()
            comparison_sparepart=get_object_or_404(queryset, pk=pk)
            serializer=LocalComparisonSparepartsSerializer(comparison_sparepart, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Successfully Updated Comparison Sparepart"}
        except:
            dict_response={'error': True, 'message':"Error During Updating Comparison Sparepart"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = Local_Comparison_SparePart.objects.all()
        comparison_sparepart=get_object_or_404(queryset, pk=pk)
        serializer=LocalComparisonSparepartsSerializer(comparison_sparepart, context={"request": request})
        return Response({'error': False, 'message':"Single Data Fetch", "data": serializer.data})

    def destroy(self, request, pk=None):
        pass


class RollerViewSet(viewsets.ViewSet):
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        roller = Roller.objects.all()
        serializer = RollerSerializer(roller, many=True, context={"request":request})
        response_dict = {"error": False, "message": "List of all roller Spareparts", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer=RollerSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Roller sparepart saved successfully"}
        except:
            dict_response={'error': True, 'message':"Error During Saving Roller Sparepart"}
        return Response(dict_response)

    def update(self, request):
        try:
            queryset = Roller.objects.all()
            roller=get_object_or_404(queryset, pk=pk)
            serializer=RollerSerializer(roller, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Successfully Updated Roller Sparepart"}
        except:
            dict_response={'error': True, 'message':"Error During Updating Roller Sparepart"}
        return Response(dict_response)

    def retrieve(self, request, pk=None):
        queryset = Roller.objects.all()
        roller=get_object_or_404(queryset, pk=pk)
        serializer=RollerSerializer(roller, context={"request": request})
        return Response({'error': False, 'message':"Single Data Fetch", "data": serializer.data})

    def destroy(self, request, pk=None):
        pass