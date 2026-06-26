from django import forms
from django.forms import inlineformset_factory
from apps.ventas.models.solicitud import SolicitudCompra, DetalleSolicitudCompra


class SolicitudCompraForm(forms.ModelForm):
    cliente_id = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del cliente'})
    )
    observaciones = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observaciones adicionales'})
    )

    class Meta:
        model = SolicitudCompra
        fields = ['cliente_id', 'observaciones']
        widgets = {
            'cliente_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID del cliente'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observaciones adicionales'}),
        }

    def clean_cliente_id(self):
        cliente_id = self.cleaned_data.get('cliente_id')
        if cliente_id is None or cliente_id < 1:
            raise forms.ValidationError('El ID del cliente debe ser un entero positivo.')
        return cliente_id

    def clean_observaciones(self):
        observaciones = self.cleaned_data.get('observaciones', '')
        return observaciones.strip()


class CheckoutSolicitudForm(forms.ModelForm):
    observaciones = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observaciones adicionales'})
    )

    class Meta:
        model = SolicitudCompra
        fields = ['observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observaciones adicionales'}),
        }


class DetalleSolicitudCompraForm(forms.ModelForm):
    producto_id = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control producto-id-input', 'placeholder': 'ID del producto'})
    )
    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control cantidad-input', 'min': '1'})
    )

    class Meta:
        model = DetalleSolicitudCompra
        fields = ['producto_id', 'cantidad']  # Cambiado de 'producto' a 'producto_id'
        widgets = {
            'producto_id': forms.NumberInput(attrs={'class': 'form-control producto-id-input', 'placeholder': 'ID del producto'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control cantidad-input', 'min': '1'}),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is None or cantidad < 1:
            raise forms.ValidationError('La cantidad debe ser al menos 1.')
        return cantidad


# Formset para poder agregar múltiples detalles en una sola solicitud
DetalleSolicitudFormSet = inlineformset_factory(
    SolicitudCompra,
    DetalleSolicitudCompra,
    form=DetalleSolicitudCompraForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True
)
