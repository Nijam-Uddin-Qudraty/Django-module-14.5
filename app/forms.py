from django import forms
from django.core import validators
from datetime import date, datetime
from .models import m_model

class homeForm(forms.Form):
    name = forms.CharField(initial='karim', help_text='enter the name', validators=
        [validators.MinLengthValidator(5, message="name mus contain at least 5 char")])
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    email = forms.EmailField(required=False)
    agree = forms.BooleanField(initial=True)
    # date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    YEARS = ['2000','2002','2004']
    date_choice = forms.DateField(widget=forms.SelectDateWidget(years= YEARS))
    date_choice1 = forms.DateField(widget=forms.SelectDateWidget())
    decimal_value = forms.DecimalField(label='Input a number')
    weight = forms.FloatField()
    message = forms.CharField(max_length=10)
    day = forms.DateField(initial=date.today)
    day1 = forms.DateTimeField( initial=datetime.today, widget= forms.DateTimeInput(attrs={'type':'datetime-local'}) )
    COLORS = [
    ('b', 'Blue'),
    ('g', 'Green'),
    ('b', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=COLORS)
    favorite_color1 = forms.ChoiceField(
        widget=forms.RadioSelect, choices=COLORS)
    favorite_colors2 = forms.MultipleChoiceField(
        choices=COLORS)
    favorite_colors3 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=COLORS)
    favorite_colors4 = forms.TypedChoiceField(
    choices=COLORS, coerce=str)
    duration = forms.DurationField( required=False)
    file = forms.FileField(disabled=True ,required=False)
    field = forms.NullBooleanField()

class m_form(forms.ModelForm):
    class Meta:
        model = m_model
        fields = '__all__'
        widgets={
            'birthday': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
