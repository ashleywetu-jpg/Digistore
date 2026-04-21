from django.contrib import admin
from django import forms
from .models import Product, PAYMENT_CHOICES

class ProductAdminForm(forms.ModelForm):
    payment_methods = forms.MultipleChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Product
        fields = '__all__'

    def clean_payment_methods(self):
        return self.cleaned_data.get('payment_methods', [])


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display  = ('name', 'price', 'is_active', 'created_at')
    list_filter   = ('is_active',)
    search_fields = ('name',)
    list_editable = ('is_active',)
