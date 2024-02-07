from django import forms
from .models import Contact,News,Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
    
class CommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'Matn kiriting',
                                                        'cols' : 30,
                                                        'rows': 5}))
    class Meta: 
        model = Comment
        fields = ('message',)