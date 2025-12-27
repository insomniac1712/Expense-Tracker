from rest_framework import serializers
from myapp.models import Expense, Category, Budget

class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.none()
    )
    
    category_name = serializers.CharField(
        source="category.name", read_only=True
    )

    class Meta:
        model = Expense
        fields = ['id','name', 'amount', 'category', 'category_name','date']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            self.fields["category"].queryset = Category.objects.filter(
                user=request.user
            )
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'category', 'amount', 'month']
        
