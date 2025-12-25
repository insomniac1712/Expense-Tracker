from django.conf import settings
from django.db import models

class Expense(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="expenses"
    )
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="expenses"
        )
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.user})"
    
    
class Category(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "name")
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Budget(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="budgets"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="budgets"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField(help_text="First day of the month for which the budget is set")

    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("user", "category", "month")
        ordering = ["-month"]

    def __str__(self):
        return f"{self.category} - {self.month}"
