from django import forms




class StudentsForm(forms.Form):
    name = forms.CharField(label='name')
    category = forms.CharField(label='category')
    expectation = forms.CharField(label='expectation')
    specialty = forms.CharField(label='specialty')
