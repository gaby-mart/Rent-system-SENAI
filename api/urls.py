from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from .views_viewset import (
    UserViewSet,
    PropertyViewSet,
    AgreementViewSet,
    PaymentViewSet
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'propertys', PropertyViewSet)
router.register(r'agreements', AgreementViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('', include(router.urls))
]