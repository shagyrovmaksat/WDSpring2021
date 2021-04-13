from django.urls import path
from api.views import companies, vacancies, vacancies_id, companies_id, top_ten_vacancies, company_vacanies

urlpatterns = [
    path('companies/', companies),
    path('companies/<int:company_id>/', companies_id),
    path('companies/<int:company_id>/vacancies', company_vacanies),
    path('vacancies/', vacancies),
    path('vacancies/<int:vacancy_id>/', vacancies_id),
    path('vacancies/top_ten/', top_ten_vacancies),
]