from .models import Quote
from .serializers import QuoteSerializer, UserSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Quote.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class PublicQuoteList(generics.ListAPIView):
    queryset = Quote.objects.filter(is_public = True)
    serializer_class = QuoteSerializer
    permission_classes = [AllowAny]

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]