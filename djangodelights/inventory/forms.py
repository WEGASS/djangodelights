from django import forms
from .models import Purchase, MenuItem

class PurchaseCreateForm(forms.ModelForm):
  class Meta:
    model = Purchase
    fields = "__all__"

  def __init__(self, *args, **kwargs):
    menu = kwargs.pop('menu')
    super(PurchaseCreateForm, self).__init__(*args, **kwargs)
    self.fields['purchased_item'].queryset = MenuItem.objects.filter(pk__in=menu)
