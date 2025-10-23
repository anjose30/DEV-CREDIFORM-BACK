from django.urls import path
from .views import V_form_create, V_form_list, V_form_retrieve, get_choice

urlpatterns = [
    path('form/create/', V_form_create.as_view()),
    path('form/list/', V_form_list.as_view()), 
    path('form/retrieve/<int:pk>/', V_form_retrieve.as_view()),
    path('form/choise/',get_choice)
]
