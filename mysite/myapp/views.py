from django.shortcuts import render,redirect, get_object_or_404
from .forms import ExpenseForm, CategoryForm, BudgetForm
from .models import Expense, Category, Budget
from django.db.models import Sum
import datetime
from django.contrib.auth.decorators import login_required
from .services import get_budget_status

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
    current_month = today.replace(day=1)
    budget_alerts = []
    budget_statuses = []
    
  
    for category in Category.objects.filter(user=request.user):
        status = get_budget_status(request.user, category, current_month)
        if status and status['exceeded']:
            budget_alerts.append({
                'category': category.name,
                'over_by': status['spent'] - status['budget']
            })
            
        if status:
            budget_statuses.append({
                'category': category.name,
                'budget': status['budget'],
                'spent': status['spent'],
                'remaining': status['remaining'],
                'exceeded': status['exceeded'],
                'percent': int((status['spent']/status['budget'])*100) if status['budget'] > 0 else 0
                
            })   
            
                
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
        'budget_alerts': budget_alerts
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

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, "myapp/budget_list.html", {"budgets": budgets})

@login_required
def budget_create(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit = False)
            budget.user = request.user
            budget.save()
            return redirect("budget_list")
    else:
        form = BudgetForm()     
    
    return render(request, "myapp/budget_form.html", {"form": form})    


