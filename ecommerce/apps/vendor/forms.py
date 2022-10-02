from django.forms import ModelForm
from apps.product.models import product

class productform(ModelForm):
    class Meta:
        model= product
        fields=['category','image','title','description','price']
