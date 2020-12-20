from rest_framework import serializers
from .models import SitesPurchaseRequest, MainPurchaseRequest


class SitePRSerializer(serializers.ModelSerializer):
    class Meta:
        model = SitesPurchaseRequest
        fields = '__all__'

class MainPRSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPurchaseRequest
        fields = '__all__'