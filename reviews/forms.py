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
        fields = ('user_profile',
                  'product',
                  'comment',
                  'stars',
                  'name',)
        # exclude = ('user_profile', 'product',)

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, remove auto-generated
            labels, and set autofocus on first field
        """
        # set up form in usual, default way
        super().__init__(*args, **kwargs)
        # define dictionary of field placeholders to be used in place of labels
        placeholders = {
            'comment': 'Your review',
            'stars': 'Rating',
            'name': 'Your name',
        }

        # Start on Comment field field when page loads
        self.fields['comment'].widget.attrs['autofocus'] = True
        # iterate through form fields adding * if required, adding custom
        # placeholder, add css for each field, and remove the default labels
        for field in self.fields:
            self.fields[field].label = False
            if field in ('user_profile', 'product'):
                self.fields[field].widget.attrs['hidden'] = True
            
            else:
                if field == 'stars':
                    self.fields[field].widget.attrs['value'] = ""
                
                placeholder = f'{placeholders[field]}'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['required'] = True
                self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
                # self.fields[field].widget.attrs['autocomplete'] = 'on'
                
