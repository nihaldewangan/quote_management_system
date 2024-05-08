from django.urls import path
from .views import CreateQuoteAPIView, ListQuotesAPIView, CreateUserAPIView, RetrieveQuoteAPIView, UpdateQuoteAPIView, DeleteQuoteAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Creating user/author
    path('qms/create_user/', CreateUserAPIView.as_view(), name='create-user'),
    # CRUD apis
    path('qms/', ListQuotesAPIView.as_view(), name='list-quotes'),
    path('qms/create/', CreateQuoteAPIView.as_view(), name='create-quote'),
    path('qms/<int:pk>/', RetrieveQuoteAPIView.as_view(), name='retrieve-quote'),
    path('qms/<int:pk>/update/', UpdateQuoteAPIView.as_view(), name='update-quote'),
    path('qms/<int:pk>/delete/', DeleteQuoteAPIView.as_view(), name='delete-quote'),
    # Token authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
