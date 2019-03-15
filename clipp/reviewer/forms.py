from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = Course
        fields = ['guid', 'title', 'description', 'status']
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        print(title)
        if "DJANGO" in title:
            return title
        else:
            raise forms.ValidationError("Not a valid title.")


class RawForm(forms.Form):
    guid = forms.CharField()
    title = forms.CharField()
    description = forms.CharField()
    status = forms.BooleanField()

