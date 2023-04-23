from django.urls import path
from api.views.provider import ProvidersView, ProviderView
from api.views.auth import OAuth2View


urlpatterns = [
    path('providers/', ProvidersView.as_view(), name="providers"),
    path('provider/', ProviderView.as_view(), name="provider-create"),
    path('provider/<int:key>/', ProviderView.as_view(), name="provider"),
    path('oauth2/code/<str:client_id>/', OAuth2View.as_view(), name="oauth2-grant")
]
