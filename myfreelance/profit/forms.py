from django import forms

from .models import *

'''
 Thanks guy jgorocica from Reddit
 to solve date input issue
 "https://www.reddit.com/r/django/comments/i7hjg9/problem_with_dateinput_in_updateview/"
'''


class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        kwargs['format'] = '%Y-%m-%d'
        super().__init__(**kwargs)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'client', 'platform', 'server', 'server_info', 'is_server_mine',
                  'rent_price', 'rent_next_payment_date', 'support', 'support_price', 'support_next_payment_date',
                  'description', 'comment', 'project_price', 'income', 'finish_date', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control text-info'}),
            'client': forms.TextInput(attrs={'class': 'form-control text-info'}),
            'platform': forms.TextInput(attrs={'class': 'form-control text-info'}),
            # 'start_date': forms.DateInput(attrs={'class': 'form-control text-info', 'type': 'date'}),

            'server': forms.TextInput(attrs={'class': 'form-control text-info'}),
            'server_info': forms.Textarea(attrs={'class': 'form-control text-info'}),
            'is_server_mine': forms.CheckboxInput(attrs={'class': 'form-control text-info'}),

            'rent_price': forms.NumberInput(attrs={'class': 'form-control text-info'}),
            'rent_next_payment_date': DateInput(attrs={'class': 'form-control text-info', 'type': 'date'}),

            'support': forms.CheckboxInput(attrs={'class': 'form-control text-info'}),
            'support_price': forms.NumberInput(attrs={'class': 'form-control text-info'}),
            'support_next_payment_date': DateInput(attrs={'class': 'form-control text-info', 'type': 'date'}),

            'description': forms.Textarea(attrs={'class': 'form-control text-info'}),
            'comment': forms.Textarea(attrs={'class': 'form-control text-info'}),

            'project_price': forms.NumberInput(attrs={'class': 'form-control text-info'}),
            'income': forms.NumberInput(attrs={'class': 'form-control text-info'}),
            # 'debt': forms.NumberInput(attrs={'class': 'form-control text-info'}),

            'finish_date': DateInput(attrs={'class': 'form-control text-info', 'type': 'date'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-control text-info'}),
        }


class PortfolioProjectForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control text-info'}))

    class Meta:
        model = Portfolio
        fields = ['name', 'project_type', 'image', 'description', 'date', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control text-info'}),
            'project_type': forms.Select(attrs={'class': 'form-control text-info'}),
            'description': forms.Textarea(attrs={'class': 'form-control text-info'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control text-info'}),
            'date': DateInput(attrs={'class': 'form-control text-info', 'type': 'date'}),
            'url': forms.URLInput(attrs={'class': 'form-control text-info'}),
        }


class AdditionalPaymentsForm(forms.ModelForm):
    class Meta:
        model = AdditionalPayments
        fields = ['project', 'price', 'description', 'comment']
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control text-info'}),
            'price': forms.NumberInput(attrs={'class': 'form-control text-info'}),
            'description': forms.Textarea(attrs={'class': 'form-control text-info'}),
            'comment': forms.Textarea(attrs={'class': 'form-control text-info'}),
        }


class SupportPaymentsForm(forms.ModelForm):
    class Meta:
        model = SupportPayments
        fields = ['project', 'price', 'description', 'comment', ]
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control text-info'}),
            'price': forms.NumberInput(attrs={'class': 'form-control text-info'}),
            'description': forms.Textarea(attrs={'class': 'form-control text-info'}),
            'comment': forms.Textarea(attrs={'class': 'form-control text-info'}),
        }
