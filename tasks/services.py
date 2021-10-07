from tasks.models import Company


def delete_company(company_id):
    company = Company.objects.get(pk=company_id)
    company.delete()