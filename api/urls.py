from django.urls import path
from api import views


urlpatterns = [
    path('providers/', views.ProvidersView.as_view(), name="providers"),
    path('provider/', views.ProviderView.as_view(), name="provider-create"),
    path('provider/<int:key>/', views.ProviderView.as_view(), name="provider")
]
