from django.forms import ModelForm
from core.models import risk


# Create the form class.
class riskForm(ModelForm):
    class Meta:
        model = risk
        fields = '__all__'