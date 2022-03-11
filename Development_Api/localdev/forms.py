
from django import forms

from .models import Call_logs

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Call_logs
        fields = '__all__'
        widgets = {
            "unique_id":forms.NumberInput(attrs={'class':'form-control'}),
            "id":forms.NumberInput(attrs={'class':'form-control'}),
            "customer_name":forms.TextInput(attrs={'class':'form-control'}),
            "customer_number":forms.NumberInput(attrs={'class':'form-control'}),
            "date":forms.TextInput(attrs={'class':'form-control'}),
            "time":forms.TextInput(attrs={'class':'form-control'}),
            "call_type":forms.TextInput(attrs={'class':'form-control'}),
            "duration":forms.NumberInput(attrs={'class':'form-control'}),
            "sales_agent_number":forms.NumberInput(attrs={'class':'form-control'}),
            "sales_agent_email":forms.TextInput(attrs={'class':'form-control'}),
            "created_at":forms.TextInput(attrs={'class':'form-control'}),

        }
