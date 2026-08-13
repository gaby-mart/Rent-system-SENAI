from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = "ADMIN", "Administrator"
        USER = "USER", "User"

    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.USER
    )

    def __str__(self):
        return self.get_full_name() or self.username


class Property(models.Model):
    # Correção: Adicionado max_length nos CharFields
    title = models.CharField(max_length=255)
    property_type = models.CharField(max_length=100)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    address = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    complement = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.title


class Agreement(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    
    # Opcional, mas comum: Vincular o imóvel ao contrato
    property = models.ForeignKey(
        Property,
        on_delete=models.PROTECT,
        related_name="agreements",
        null=True, blank=True # Remova o null/blank se o contrato SEMPRE precisar de um imóvel
    )
    
    # Correção: Ajustado on_delete para PROTECT e related_name para nomes mais claros
    lessor = models.ForeignKey(
        User,
        related_name="lessor_agreements",
        on_delete=models.PROTECT
    )
    renter = models.ForeignKey(
        User,
        related_name="renter_agreements",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Agreement {self.id}"


class Payment(models.Model):
    payment_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    
    # Correção: related_name alterado para 'payments'
    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    def __str__(self):
        return f"Payment No. {self.id}"