from django.urls import path
from api.views.provider import ProvidersView, ProviderView
from api.views.auth import AuthenticationView


urlpatterns = [
    path('providers/', ProvidersView.as_view(), name="providers"),
    path('provider/', ProviderView.as_view(), name="provider-create"),
    path('provider/<int:key>/', ProviderView.as_view(), name="provider"),
    path('authorize/<str:name>/', AuthenticationView.as_view(), name="authorize"),
    path('authenticate/<str:name>/', AuthenticationView.as_view(), name="authenticate")
]
