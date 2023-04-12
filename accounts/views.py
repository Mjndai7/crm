# Create your views here.
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from .models import employeeProfile, employeeDetails
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import employeeProfileSerializer, employeeDetailsSerializer

class employeeProfileListCreateView(ListCreateAPIView):
    queryset = employeeProfile.objects.all()
    serializer_class = employeeProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
    
class employeeProfileDetailView(RetrieveUpdateDestroyAPIView):

    queryset = employeeProfile.objects.all()
    serializer_class = employeeProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

# HR Info
class employeeDetailsListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    # permission_classes = (AllowAny, )

    serializer_class = employeeDetailsSerializer
    queryset = employeeDetails.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(name=user)

class employeeDetailsDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    # permission classes = (AllowAny, )

    serializer_class = employeeDetailsSerializer
    queryset = employeeDetails.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(name=user)
 

