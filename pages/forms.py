from django import forms

class contact_form(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.CharField(max_length=500, label="Email")
    comment= forms.CharField(label='',widget=forms.Textarea(
                        attrs={'placeholder': 'Was willst du uns mitteilen?'}))