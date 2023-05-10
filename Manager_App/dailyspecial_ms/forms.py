from django import forms
from .models import DailySpecial


class DailySpecialForm(forms.ModelForm):
    class Meta:
        model = DailySpecial
        fields = ['menu', 'offers', 'discounts']
        labels = {
            'menu': 'Today\'s Special Menu',
            'offers': 'Today\'s Special Offers',
            'discounts': 'Today\'s Special Discounts',
        }
        widgets = {
            'offers': forms.Textarea(attrs={'rows': 5}),
            'discounts': forms.Textarea(attrs={'rows': 5}),
        }
