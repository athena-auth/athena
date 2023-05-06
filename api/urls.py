from django.urls import path
from api.views.provider import ProvidersView, ProviderView
from api.views.auth import AuthorizationView


urlpatterns = [
    path('providers/', ProvidersView.as_view(), name="providers"),
    path('provider/', ProviderView.as_view(), name="provider-create"),
    path('provider/<int:key>/', ProviderView.as_view(), name="provider"),
    path('authorize/<str:name>/', AuthorizationView.as_view(), name="authorize")
]
