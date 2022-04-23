from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Quote(models.Model):

    id = models.AutoField(primary_key=True)
    quote = models.TextField("QUOTE")
    user = models.ForeignKey(verbose_name="Author", to=User, on_delete=models.CASCADE, related_name="info_users")
    
    # for more info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
        return f"{self.user} {self.quote} {self.id}"