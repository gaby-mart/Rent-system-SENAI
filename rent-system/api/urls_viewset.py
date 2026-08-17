from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views_viewset import *

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'propertys', PropertyViewSet)
router.register(r'agreements', AgreementViewSet)
router.register(r'payments', PaymentViewSet)


urlpatterns = [
    path('api/viewset/', include('api.urls_viewset')),
]