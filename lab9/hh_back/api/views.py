from django.http.response import JsonResponse
from api.models import Vacancy, Company

def companies(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def companies_id(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(company.to_json())

def company_vacanies(request, company_id):
    try:
        vacancies = Vacancy.objects.filter(company=company_id)
    except Exception as e:
        return JsonResponse({'message': str(e)})

    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancies_id(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(vacancy.to_json())

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by("-salary")[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)