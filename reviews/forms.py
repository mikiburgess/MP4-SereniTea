"""
Review forms for "SERENITEA EMPORIUM"
- - - - - - - - - - - - - - - - - - - -
"""
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        # only show the fields user needs to edit
        fields = ('product',
                  'comment',
                  'stars',
                  'name',)
        # exclude = ('product',)

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, remove auto-generated
            labels, and set autofocus on first field
        """
        # set up form in usual, default way
        super().__init__(*args, **kwargs)
        # define dictionary of field placeholders to be used in place of labels
        placeholders = {
            'product': 'Product',
            'comment': 'Your review',
            'stars': 'Star rating',
            'name': 'Your name',
        }

        # Start on Comment field field when page loads
        self.fields['comment'].widget.attrs['autofocus'] = True
        # iterate through form fields adding * if required, adding custom
        # placeholder, add css for each field, and remove the default labels
        for field in self.fields:
            # if field != 'profile':
            #     if self.fields[field].required:
            #         placeholder = f'{placeholders[field]} *'
            #     else:
            #         placeholder = 'Product'
            placeholder = f'{placeholders[field]}  *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].widget.attrs['autocomplete'] = 'on'
            self.fields[field].label = False
