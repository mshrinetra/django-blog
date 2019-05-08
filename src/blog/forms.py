from django import forms
from .models import BlogPost


class NewBlogForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control mb-4', 'placeholder': 'Title'}))
    slug = forms.SlugField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control mb-4', 'placeholder': 'Slug'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control mb-4'}))


class NewBlogModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control mb-4', 'placeholder': 'Title'}))
    slug = forms.SlugField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control mb-4', 'placeholder': 'Slug'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control mb-4'}))

    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']

    # validation
    def clean_title(self, *args, **kwargs):
        instance = self.instance    # For update
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title has already been used")
        return title
