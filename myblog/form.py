from django import forms
from mdeditor.fields import MDTextFormField


class CreateBugForm(forms.Form):
    # https://zhuanlan.zhihu.com/p/55158579
    bug_detail = MDTextFormField(label="", widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=65535)
