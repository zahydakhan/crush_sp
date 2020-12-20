from rest_framework import viewsets, generics
from rest_framework.response import Response
from DjangoMedicalApp.models import Company,CompanyBank, Medicine
from DjangoMedicalApp.serializers import CompanySerializer, CompanyBankSerializer, MedicineSerializer, MedicalDetailsSerializer, MedicalDetailSerializerSimple
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={"request":request})
        response_dict = {"error": False, "message": "All company List Data", "data":serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer=CompanySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Company data saved successfully"}
        except:
            dict_response={'error': True, 'message':"Error During Saving Company Data"}
        return Response(dict_response)

    def update(self, request):
        try:
            queryset = Company.objects.all()
            company=get_object_or_404(queryset, pk=pk)
            serializer=CompanySerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Successfully Updated Company Data"}
        except:
            dict_response={'error': True, 'message':"Error During Updating Company Data"}
        return Response(dict_response)

company_list=CompanyViewSet.as_view({"get":'list'})
company_create=CompanyViewSet.as_view({"post":'create'})
company_update=CompanyViewSet.as_view({'put':'update'})

class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        try:
            serializer=CompanyBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Company data saved successfully"}
        except:
            dict_response={'error': True, 'message':"Error During Saving Company Bank Data"}
        return Response(dict_response)

    def list(self, request):
        companybank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(companybank, many=True, context={"request":request})
        response_dict = {"error": False, "message": "All company bank list data", "data":serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        companybank=get_object_or_404(queryset, pk=pk)
        serializer=CompanyBankSerializer(companybank, context={"request": request})
        return Response({'error': False, 'message':"Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset=CompanyBank.objects.all()
            companybank=get_object_or_404(queryset, pk=pk)
            serializer=CompanyBankSerializer(companybank, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Data has been updated"}
        except:
            dict_response={'error': True, 'message':"Error During Updating Company Data"}
        return Response(dict_response)

class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer
    def get_queryset(self):
        name=self.kwargs["name"]
        return Company.objects.filter(name__icontains=name)

class MedicineViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        try:
            serializer=MedicineSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            medicine_id=serializer.data['id'];
            print(medicine_id)
            medicine_details_list=[]
            for medicine_detail in request.data["medicine_details"]:
                print(medicine_detail)
                medicine_detail["medicine_id"]=medicine_id
                medicine_details_list.append(medicine_detail)
                print(medicine_detail)

            serializer2=MedicalDetailsSerializer(data=medicine_details_list, many=True, context={"request":request})
            serializer2.is_valid()
            serializer2.save()
            dict_response={"error": False, "message": "Medicine data saved successfully"}

        except:
            dict_response={'error': True, 'message':"Error During Saving Medicine Data"}
        return Response(dict_response)

    def list(self, request):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer(medicine, many=True, context={"request":request})
        medicine_data=serializer.data
        newmedicinelist=[]

        for medicine in medicine_data:
            medicine_details=MedicalDetails.objects.filter(medicine_id=medicine["id"])
            medicine_details_serializers=MedicalDetailSerializerSimple(medicine_deails, many=True)
            medicine["medicine_details"]=medicine_details_serializer.data
            newmedicinelist.append(medicine)

        response_dict = {"error": False, "message": "All medicine list data", "data":newmedicinelist}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Medicine.objects.all()
        medicine=get_object_or_404(queryset, pk=pk)
        serializer=MedicineSerializer(medicine, context={"request": request})
        serializer.data=serializer.data
        medicine_details = MedicalDetails.objects.filter(medicine_id=serializer_data["id"])
        medicine_details_serializers=MedicalDetailsSerializerSimple(medicine_details, many=True)
        serializer_data["medicine_details"] = medicine_details_serializers.data
        return Response({'error': False, 'message':"Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset=Medicine.objects.all()
            companybank=get_object_or_404(queryset, pk=pk)
            serializer=MedicineSerializer(medicine, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error": False, "message": "Data has been updated"}
        except:
            dict_response={'error': True, 'message':"Error During Updating Company Data"}
        return Response(dict_response)




