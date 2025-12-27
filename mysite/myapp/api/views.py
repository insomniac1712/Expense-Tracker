from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from myapp.models import Expense, Category, Budget
from .serializers import ExpenseSerializer, CategorySerializer, BudgetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
import datetime
from django_filters.rest_framework import DjangoFilterBackend


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filter_backenfds = [DjangoFilterBackend]
    filterset_fields = ['category', 'date']

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class BudgetViewSet(ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class ExpenseAnalyticsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        expenses = Expense.objects.filter(user=request.user)
        today = datetime.date.today()

        return Response({
            "total": expenses.aggregate(total=Sum("amount"))["total"] or 0,
            "monthly": expenses.filter(
                date__gte=today - datetime.timedelta(days=30)
            ).aggregate(total=Sum("amount"))["total"] or 0,
            "weekly": expenses.filter(
                date__gte=today - datetime.timedelta(days=7)
            ).aggregate(total=Sum("amount"))["total"] or 0,
        })
    
