from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name="vacancies")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.to_json(),
        }

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"