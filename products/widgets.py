from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as gtl


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = gtl('Remove')
    initial_text = gtl('Current Image')
    input_text = gtl('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
