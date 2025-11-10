# main/forms.py
# from django import forms
# from .models import Post
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'description', 'image', 'video']


from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'mobile', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Mobile'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        message = cleaned_data.get("message")

        if not name or not email or not message:
            raise forms.ValidationError("Name, Email, and Message are required fields.")


