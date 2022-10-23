from rest_framework import serializers 
from .models import Applicants 


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Applicants
        # fields= ' __all__ '
        fields = ['id','firstname','lastname', 'email','phone', 'amount','address', 'course', 'center', 'mode']




