from django.shortcuts import render,redirect, get_object_or_404
from .forms import ExpenseForm, CategoryForm
from .models import Expense, Category
from django.db.models import Sum
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("index")


    # ONLY current user's expenses
    expenses = Expense.objects.filter(user=request.user)

    total_expenses = expenses.aggregate(total=Sum('amount'))

    today = datetime.date.today()

    yearly_sum = expenses.filter(
        date__gt=today - datetime.timedelta(days=365)
    ).aggregate(total=Sum('amount'))

    monthly_sum = expenses.filter(
        date__gt=today - datetime.timedelta(days=30)
    ).aggregate(total=Sum('amount'))

    weekly_sum = expenses.filter(
        date__gt=today - datetime.timedelta(days=7)
    ).aggregate(total=Sum('amount'))

    daily_sums = (
        expenses
        .values('date')
        .order_by('date')
        .annotate(total=Sum('amount'))
    )

    categorical_sums = (
        expenses
        .values('category__name')
        .order_by('category__name')
        .annotate(total=Sum('amount'))
    )

    expense_form = ExpenseForm()

    return render(request, 'myapp/index.html', {
        'expense_form': expense_form,
        'expenses': expenses,
        'total_expenses': total_expenses,
        'yearly_sum': yearly_sum,
        'monthly_sum': monthly_sum,
        'weekly_sum': weekly_sum,
        'daily_sums': daily_sums,
        'categorical_sums': categorical_sums,
    })


@login_required
def edit(request, id):
    expense = get_object_or_404(
        Expense,
        id=id,
        user=request.user
    )

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'myapp/edit.html', {
        'expense_form': form
    })


@login_required
def delete(request, id):
    expense = get_object_or_404(
        Expense,
        id=id,
        user=request.user
    )

    if request.method == "POST":
        expense.delete()

    return redirect('index')


@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'myapp/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'myapp/category_form.html', {'form': form})

@login_required
def category_delete(request, id):
    category = get_object_or_404(
        Category,
        id=id,
        user=request.user
    )
    
    if request.method == "POST":
        category.delete()

    return redirect("category_list")
