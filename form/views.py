from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view

from django.db.models import Q

from .serializers import Sz_form_create, Sz_form_list, Sz_form_retrieve
from.models import M_form
# Create your views here.

class Limit_paginator(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20

class V_form_create(CreateAPIView):
    serializer_class = Sz_form_create
    model_class = M_form
    
    def perform_create(self, serializer):
        return serializer.save()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        error = {
            'error': serializer.errors,
            'message':'Error al crear el formulario'
        }
        
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    
class V_form_list(ListAPIView):
    serializer_class = Sz_form_list
    pagination_class = Limit_paginator
    
    def get_queryset(self):
        queryset = M_form.objects.all()
        query = self.request.query_params.get('query', None)
        search_field = self.request.query_params.get('search_field', None)
        ordering = self.request.query_params.get('ordering', None)
        
        if query:
            if search_field == 'name':
                queryset = queryset.filter(Q(name__icontains=query) | Q(last_name__icontains=query))
            elif search_field == 'id_number':
                queryset = queryset.filter(id_number__istartswith=query)
            elif search_field == 'point':
                queryset = queryset.filter(adviser__icontains=query)
            else:
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(last_name__icontains=query) |
                    Q(id_number__istartswith=query) |
                    Q(adviser__icontains=query)
                )

        if ordering:
            allowed = {'create_at', '-create_at', 'credit_value', '-credit_value'}
            if ordering in allowed:
                queryset = queryset.order_by(ordering)
            else:
                queryset = queryset.order_by('-id')
        else:
            queryset = queryset.order_by('-id')

        return queryset

class V_form_retrieve(RetrieveAPIView):
    serializer_class = Sz_form_retrieve
    model_class = M_form
    queryset = model_class.objects.all()


@api_view(['GET'])    
def get_choice(request):
    id_type = dict(M_form.id_type_choice)
    response = {
        "id_type_choice":id_type
    }
    return Response(response, status=status.HTTP_200_OK)