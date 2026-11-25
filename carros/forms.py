from django import forms

from .models import Carro


class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = [
            'marca', 'modelo', 'ano', 'preco', 'km', 'cor',
            'potencia_cv', 'velocidade_max', 'zero_a_cem',
            'cambio', 'cidade', 'descricao', 'imagem',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_imagem(self):
        img = self.cleaned_data.get('imagem')
        # só valida quando é um arquivo novo enviado agora
        if img and hasattr(img, 'content_type'):
            if img.size > 5 * 1024 * 1024:
                raise forms.ValidationError('A imagem deve ter no máximo 5 MB.')
            if not img.content_type.startswith('image/'):
                raise forms.ValidationError('Envie um arquivo de imagem.')
        return img