from django.forms import ModelForm
from main_app.models import TODO
class TODOForm(ModelForm):
    class  Meta:
        model = TODO
        fields = ['title','description','is_completed']
