from django import forms
from ..models import Venta


class VentaForm(forms.ModelForm):
    cliente_id = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del cliente'})
    )
    total = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )
    vendedor_id = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del vendedor'})
    )

    class Meta:
        model = Venta
        fields = ['cliente_id', 'total', 'vendedor_id']
        widgets = {
            'cliente_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del cliente'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'vendedor_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del vendedor'}),
        }

    def clean_cliente_id(self):
        cliente_id = self.cleaned_data.get('cliente_id')
        if cliente_id is None or cliente_id < 1:
            raise forms.ValidationError('El ID del cliente debe ser un entero positivo.')
        return cliente_id

    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total is not None and total <= 0:
            raise forms.ValidationError('El total debe ser un valor positivo mayor que cero.')
        return total

    def clean_vendedor_id(self):
        vendedor_id = self.cleaned_data.get('vendedor_id')
        if vendedor_id is None or vendedor_id < 1:
            raise forms.ValidationError('El ID del vendedor debe ser un entero positivo.')
        return vendedor_id


class CheckoutVentaForm(forms.ModelForm):
    total = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )

    class Meta:
        model = Venta
        fields = ['total']
        widgets = {
            'total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
