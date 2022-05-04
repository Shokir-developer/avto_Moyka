from django import forms
from .models import Mijoz

class MijozForm(forms.ModelForm):
	class Meta:
		model = Mijoz
		fields = '__all__'

		widgets = {
		'nomer':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Mashina nomerini kiriting','style':'height:60px;font-size:24px;'}),
		}