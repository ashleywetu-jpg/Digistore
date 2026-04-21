from django.db import models

PAYMENT_CHOICES = [
    ('mpesa', 'M-Pesa'),
    ('paypal', 'PayPal'),
    ('bank', 'Bank Transfer'),
    ('cash', 'Cash on Delivery'),
    ('card', 'Debit/Credit Card'),
]

class Product(models.Model):
    name          = models.CharField(max_length=200)
    description   = models.TextField(blank=True)
    price         = models.DecimalField(max_digits=10, decimal_places=2)
    image         = models.ImageField(upload_to='products/', blank=True, null=True)
    payment_methods = models.JSONField(
        default=list,
        help_text="Select accepted payment methods"
    )
    is_active     = models.BooleanField(default=True)
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_payment_labels(self):
        label_map = dict(PAYMENT_CHOICES)
        return [label_map.get(m, m) for m in self.payment_methods]

    def formatted_price(self):
        return f"KSh {self.price:,.0f}"
