from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["fullname", "lastname", "address", "age", "mobilenumber",]
    labels = {'fullname': "FullName", 'lastname': "LastName", 'address': "Address", 'age': "Age", "mobilenumber": "Mobile Number",}
