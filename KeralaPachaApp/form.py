from django import forms
from KeralaPachaApp.models import Order_Details

class CreateOrder(forms.ModelForm): 


    class Meta:
        model = Order_Details
        exclude = ("Is_whole_price", "Is_discounted","Discount","Price_After_Discount","Total" )
        fields = '__all__'
        widgets ={
            'Date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

       
     