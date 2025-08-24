from django import forms
from .models import Portfolio
# so mr Aryan here you list them all the fields you want to be editable in the form
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['stocks', 'liquid_cash', 'bank']