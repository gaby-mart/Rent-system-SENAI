from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *
from .filters import UserFilter, PropertyFilter, AgreementFilter, PaymentFilter


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAdminUser]
    )
    def names(self, request):
        users = self.get_queryset()
        names = [
            user.get_full_name().strip() or user.username
            for user in users
        ]
        return Response(names)


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyFilter

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAdminUser]
    )
    def titles(self, request):
        properties = self.get_queryset()
        list_titles = [
            prop.title.strip() if hasattr(prop, 'title') else prop.get_title().strip()
            for prop in properties
        ]
        return Response(list_titles)


class AgreementViewSet(ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AgreementFilter

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAdminUser]
    )
    def details(self, request):
        # select_related otimiza a busca das chaves estrangeiras (lessor e renter)
        agreements = self.get_queryset().select_related('lessor', 'renter')
        list_details = [
            {
                "id": agreement.id,
                "lessor": agreement.lessor.get_full_name().strip() or agreement.lessor.username,
                "renter": agreement.renter.get_full_name().strip() or agreement.renter.username,
            }
            for agreement in agreements
        ]
        return Response(list_details)


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter

    @action(
        detail=False,
        methods=['get'],
        url_path='details-payments',  # Padroniza a URL usando hífen em vez de underline
        permission_classes=[IsAdminUser]
    )
    def details_payments(self, request):
        payments = self.get_queryset()
        list_payments = [
            {
                "value": getattr(payment, 'price', getattr(payment, 'value', None)),
                "payment_date": payment.payment_date
            }
            for payment in payments
        ]
        return Response(list_payments)