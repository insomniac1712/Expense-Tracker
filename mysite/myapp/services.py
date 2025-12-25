from django.db.models import Sum
import datetime
from .models import Expense, Budget, Category

def get_budget_status(user, category, month):
    start = month.replace(day=1)
    end = (start + datetime.timedelta(days=32)).replace(day=1)

    spent = (
        Expense.objects
        .filter(
            user=user,
            category=category,
            date__gte=start,
            date__lt=end
        )
        .aggregate(total=Sum("amount"))["total"] or 0
    )

    budget = Budget.objects.filter(
        user=user,
        category=category,
        month=start
    ).first()

    if not budget:
        return None

    return {
        "budget": budget.amount,
        "spent": spent,
        "remaining": budget.amount - spent,
        "exceeded": spent > budget.amount
    }

