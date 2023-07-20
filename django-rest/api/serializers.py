from rest_framework import serializers
from .models import Student

"""
# Validators
def starts_with_s(value):
    if value[0].lower() != 's':
        raise serializers.ValidationError('Name Should Starts With S')
    return value
 
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[starts_with_s,])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    
    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Admission Already Closed')
        return value
    
    # Object Level Validation
    def validate(self, data): 
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'thousi' and ct.lower() != 'Payyannur':
            raise serializers.ValidationError('City Must be Payyannur')
        return data
"""
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # extra_kwargs = {'name':{'read_only':True}}
        
    def validate_roll(self, value):
        if value >= 200:
             serializers.ValidationError('Admission Already Closed')
        return value
        
        