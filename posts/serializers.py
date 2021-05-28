from rest_framework import serializers
from posts.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    appraisal_amount = serializers.SerializerMethodField()
    emp_phone = serializers.ReadOnlyField(source='phone')
    emp_phone1 = serializers.CharField(source='phone')

    class Meta:
        model = Employee
        fields = ['name', 'email', 'appraisal_amount', 'emp_phone', 'emp_phone1']
        # fields = '__all__'
    
    def get_appraisal_amount(self, instance):
        return 0.1 * instance.salary

class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'