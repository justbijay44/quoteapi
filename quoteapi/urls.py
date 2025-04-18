from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from quoteapi.quote.views import (QuoteViewSet, PublicQuoteList, RegisterView)

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet, basename= 'quotes' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/public-quotes/', PublicQuoteList.as_view(), name='public_quotes'),
    path('api/register/', RegisterView.as_view(), name='register'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh
]
