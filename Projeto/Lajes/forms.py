from django import forms
from .models import Laje
class Lajeform(forms.ModelForm):
class Meta:
	model = Laje
	fields = '_all_'


	"""docstring for Lajeform"forms.ModelFormf 
class Meta:
	model = Laje
	fields = '_all_'

	__init__(self, arg):
		super Lajeform,forms.ModelForm._
class Meta:
	model = Laje
	fields = '_all_'

		_init__()
		self.arg = arg
		