from django import forms
from .models import Product, Category, Sub_Category, Articles, Gender

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = "__all__"

    def __init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # friendly_names = [ (c.pk, c.get_friendly_name()) for c in categories ]
        # self.fields['categories'].choices = friendly_names
        #
        """ Hola """
        for field_name, field in self.fields.items():
            field.fields.widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['placeholder'] = field.label
