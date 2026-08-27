from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.db.models import Count

from io import BytesIO

import matplotlib.pyplot as plt

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

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAdminUser]
    )  
    def graphic(self, request):
        data = ( Property.objects.values("property_type").annotate(totals=Count("id"))
        )

        types = [item["property_type"]for item in data]

        totals = [item['totals'] for item in data]

        plt.bar(types, totals)
        plt.title("Real estate Longitude")
        plt.xlabel("Types")
        plt.ylabel("amount")

        image = BytesIO()
        plt.savefig(image, format = "png")
        plt.close()
        image.seek(0)

        return HttpResponse(image, content_type="image/png")

    @action(
            detail=False,
            methods=['get'],
            permission_classes=[IsAdminUser]
        )  
    def grafico(self, request):
        data = ( Property.objects.values("property_type").annotate(totals=Count("id"))
        )
    
        types = [item["property_type"]for item in data]
    
        totals = [item['totals'] for item in data]

        fig, ax = plt.subplots()

        bar_labels = ['pink', 'blue', 'purple']
        bar_colors = ['tab:pink', 'tab:blue', 'tab:purple']

        ax.bar(types, totals, label=bar_labels, color=bar_colors)

        ax.set_ylabel('BRZ Real Estate')
        ax.set_title('Properties supply by kind and color')
        ax.legend(title='Types Properties color')
        fig.tight_layout()

        image = BytesIO()

        fig.savefig(
            image,
            format='png'
        )

        plt.close(fig)

        image.seek(0)

        return HttpResponse(image.getvalue(), content_type="image/png")

    @action(
            detail=False,
            methods=['get'],
            permission_classes=[IsAdminUser]
        )  
    def grafico_pizza(self, request):
        data = ( Property.objects.values("property_type").annotate(totals=Count("id"))
        )
    
        types = [item["property_type"]for item in data]
    
        totals = [item['totals'] for item in data]

        fig, ax = plt.subplots()

        image = BytesIO()

        ax.pie(
        totals,
        labels=types,
        autopct='%1.1f%%',
        colors=['pink', 'blue', 'purple']
        )

        ax.set_title('BRZ Real Estate')

        fig.savefig(
            image,
            format='png'
        )

        plt.close(fig)

        image.seek(0)

        return HttpResponse(image.getvalue(), content_type="image/png")



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