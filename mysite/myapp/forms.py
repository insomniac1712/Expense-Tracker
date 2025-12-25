from django import forms
from django.forms import ModelForm
from .models import Expense, Category, Budget

class ExpenseForm(ModelForm):
    class Meta: 
        model = Expense
        fields = ('name','amount','category')
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'amount', 'month']