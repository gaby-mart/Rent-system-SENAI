from rest_framework.urls import path

from .views_generics import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path("users", UserListCreateGeneric.as_view()),
    path("users/<int:pk>", UserUpdateDestroyGeneric.as_view()),
    path("propertys", PropertyListCreateGeneric.as_view()),
    path("propertys/<int:pk>", PropertyUpdateDestroyGeneric.as_view()),
    path("agrrements", AgreementListCreateGeneric.as_view()),
    path("agrrements", AgreementUpdateDestroyGeneric.as_view()),
    path("payments", PaymentListCreateGeneric.as_view()),
    path("payments", PaymentUpadateDestroyGeneric.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]