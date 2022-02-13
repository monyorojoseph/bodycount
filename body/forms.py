from .models import Person, Review
from django.forms import ModelForm

# model forms
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"