from django import forms
from django.forms import ModelForm

from RecordApp.models import Status, TransactionType, Category, SubCategory, DDSRecord


class StatusForm(ModelForm):
    class Meta:
        fields = ['status_name']
        model = Status

class TransactionTypeForm(ModelForm):
    class Meta:
        fields = ['type_name']
        model = TransactionType

class CategoryForm(ModelForm):
    class Meta:
        fields = ['category_name', 'type_model']
        model = Category
        widgets = {
            'type_model': forms.Select(attrs={'class': 'form-select'}),
        }

class SubCategoryForm(ModelForm):
    class Meta:
        fields = ['subcategory_name', 'category']
        model = SubCategory
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'})
        }

class DDSRecordForm(ModelForm):
    class Meta:
        model = DDSRecord
        fields = ['status', 'type_model', 'category', 'subcategory', 'sum_amount', 'comment']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'type_model': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'sum_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }