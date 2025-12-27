from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, CategoryViewSet, BudgetViewSet, ExpenseAnalyticsAPI

router = DefaultRouter()
router.register(r"expenses", ExpenseViewSet, basename="expense")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"budgets", BudgetViewSet, basename="budget")

urlpatterns = router.urls

urlpatterns += [
    path("analytics/", ExpenseAnalyticsAPI.as_view(), name="expense-analytics"),
]