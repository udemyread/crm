from rest_framework import viewsets, generics, status
from rest_framework.permissions import AllowAny
from .models import User, Client, Order, Interaction
from .serializers import UserSerializer, ClientSerializer, OrderSerializer, InteractionSerializer, RegisterSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=False, methods=['get'], url_path='stats', renderer_classes=[JSONRenderer])
    def stats(self, request):
        total_clients = Client.objects.count()
        return Response({'total_clients': total_clients}, status=status.HTTP_200_OK)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
