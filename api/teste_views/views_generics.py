from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..models import *
from ..serializers import *

class UserListCreateGeneric(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PropertyListCreateGeneric(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyUpdateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class AgreementListCreateGeneric(ListCreateAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

class AgreementUpdateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

class PaymentListCreateGeneric(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
class PaymentUpadateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
