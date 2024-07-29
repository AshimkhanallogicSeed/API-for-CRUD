from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import company_list

@method_decorator(csrf_exempt, name='dispatch')
class CompanyListView(View):
    
    def get(self, request):
        companies = company_list.objects.all().values()
        return JsonResponse(list(companies), safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        company = company_list.objects.create(
            compName=data.get('compName'),
            compAddress=data.get('compAddress'),
            compCity=data.get('compCity'),
            compState=data.get('compState'),
            compURL=data.get('compURL'),
            compEstd=data.get('compEstd'),
            compType=data.get('compType'),
            compSize=data.get('compSize'),
            compISIN=data.get('compISIN'),
        )
        return JsonResponse({"id": company.compID})
    
    def put(self, request, compID):
        data = json.loads(request.body)
        company = company_list.objects.get(compID=compID)
        company.compName = data.get('compName', company.compName)
        company.compAddress = data.get('compAddress', company.compAddress)
        company.compCity = data.get('compCity', company.compCity)
        company.compState = data.get('compState', company.compState)
        company.compURL = data.get('compURL', company.compURL)
        company.compEstd = data.get('compEstd', company.compEstd)
        company.compType = data.get('compType', company.compType)
        company.compSize = data.get('compSize', company.compSize)
        company.compISIN = data.get('compISIN', company.compISIN)
        company.save()
        return JsonResponse({"id": company.compID})
    
    def delete(self, request, compID):
        company = company_list.objects.get(compID=compID)
        company.delete()
        return JsonResponse({"id": compID})
