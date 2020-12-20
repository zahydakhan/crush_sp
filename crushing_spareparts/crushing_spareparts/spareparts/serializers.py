from rest_framework import serializers
from .models import SparePart, Local_Comparison_SparePart, Roller


class LocalComparisonSparepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local_Comparison_SparePart
        fields = '__all__'

class SparePartSerializer(serializers.ModelSerializer):
    comparison_sparepart = LocalComparisonSparepartsSerializer( many=True, read_only=True)
    class Meta:
        model = SparePart
        fields = '__all__'

class RollerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roller
        fields = '__all__'