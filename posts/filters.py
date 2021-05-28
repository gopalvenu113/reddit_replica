from django.db.models import query
from rest_framework import fields
from posts.models import Employee
import django_filters


class EmployeeFilterSet(django_filters.FilterSet):
    emp_name = django_filters.CharFilter(name='name')
    emp_email = django_filters.CharFilter(name='email')
    appraisal = django_filters.MethodFilter(action='get_apprailsal_filter')

    class Meta:
        model = Employee
        fields = {'salary': ['gt', 'lt']}
    
    def get_apprailsal_filter(self, queryset, value):
        queryset = queryset.filter(salary__gt=value)
        return queryset