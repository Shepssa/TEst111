from django import forms
from inbox.models import Customer


class InboxForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True, max_length=50)
    phone = forms.CharField(required=True, max_length=50)

    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ("product",)
