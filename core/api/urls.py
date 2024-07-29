from django.urls import path
from .views import CompanyListView

urlpatterns = [
    path('company/', CompanyListView.as_view(), name='company_list_create'),
    path('company/<int:compID>/', CompanyListView.as_view(), name='company_detail'),
]
