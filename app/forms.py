from django.forms import ModelForm
from .models import Question, Donation

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'