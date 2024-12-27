from django import forms
from main.models import *

class MahsulotForm(forms.ModelForm):
    class Meta:
        model=Mahsulot
        fields='__all__'
class MijozForm(forms.ModelForm):
    class Meta:
        model=Mijoz
        fields='__all__'
class BuyurtmaForm(forms.ModelForm):
    class Meta:
        model=Buyurtma
        fields='__all__'