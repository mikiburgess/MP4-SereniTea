"""
Review Form for "SERENITEA EMPORIUM"
 - using Django Form building
- - - - - - - - - - - - - - - - - - - -
"""
from django import forms
from .models import Review, Product


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # only show the fields user needs to edit
        fields = ('user_profile', 'product',
                  'stars',
                  'comment',
                  'name',)
        # exclude = ('user_profile', 'product',)

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, remove auto-generated
            labels, and set autofocus on first field
        """
        # start up form in usual, default way
        super().__init__(*args, **kwargs)
        # define dictionary of field placeholders to be used in place of labels        
        placeholders = {
            'user_profile': 'User', 
            'product': 'Product',
            'stars': 'Star rating',
            'comment': 'Your review',
            'name': 'Your name',
        }

        # Start on Full Name field when page loads
        # self.fields['comment'].widget.attrs['autofocus'] = True
        # self.fields['product'].widget.attrs['value'] = self.product.name
        # iterate through form fields adding * if required, adding custom
        # placeholder, add css for each field, and remove the default labels
        for field in self.fields:
            placeholder = f'{placeholders[field]}'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False


