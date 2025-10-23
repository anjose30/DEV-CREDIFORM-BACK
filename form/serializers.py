from rest_framework import serializers
from .models import M_form

class Sz_form_create(serializers.ModelSerializer):
    class Meta:
        model = M_form
        fields = [
            'name',
            'last_name',
            'id_type',
            'id_number',
            'credit_value',
            'interest',
            'months',
            'adviser',
        ]
        
class Sz_form_list(serializers.ModelSerializer):
    class Meta:
        model = M_form
        fields = [
            'id',
            'name',
            'last_name',
            'id_number',
            'credit_value',
            'months',
            'adviser',
            'create_at'
        ]
        read_only_fields = fields
        
class Sz_form_retrieve(serializers.ModelSerializer):
    class Meta:
        model = M_form
        fields = [
            'id',
            'name',
            'last_name',
            'id_type',
            'id_number',
            'credit_value',
            'interest',
            'months',
            'adviser',
            'create_at'
        ]
        read_only_fields = fields