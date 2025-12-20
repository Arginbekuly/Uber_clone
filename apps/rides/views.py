# Django modules
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import QuerySet

# Django Rest framework modules
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request as DRFRequest
from rest_framework.response import Response as DRFResponse
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status

# Project modules
from .models import Ride, Vehicle 
from .serializers import RideSerializer, VehicleSerializer

class RideViewSet(ViewSet):
    """
    View Set for Ride model
    """

    def list(self, request: DRFRequest) -> DRFResponse :
        """
        Returns a list of Ride objects.

        Args:
            request(Request):The HTTP request objects;

        Returns:
            List of serialized rides
        """

        rides = Ride.objects.select_related("driver", "passenger").all()
        serializer = RideSerializer(rides, many = True)
        return DRFResponse(serializer.data)
    
    def retrieve(self, request: DRFRequest, pk: int = None) -> DRFResponse:
        """
        Retrieve a single Ride by pk.

        Args:
            request(Request) The HTTP request objects.
            pk (int) :Primary key of the Ride.

        Returns:
            Response: Serialized Ride objects or 404 if not found. 
        """

        try:
            ride = Ride.objects.select_related("driver", "passenger").get(pk = pk)
        except Ride.DoesNotExist:
            return DRFResponse({"detail": "Not found."}, status = status.HTTP_404_NOT_FOUND)
        serializer = RideSerializer(ride)
        return DRFResponse(serializer.data)
    
    def create(self, request: DRFRequest) -> DRFResponse:
        """
        Create a new Ride objects

        Args:
            request(Request) The HTTP request objects containing ride data.

        Returns:
            Response: Serialized Ride objects if created or 400 if validation error. 
        """

        serializer = RideSerializer(data = request.data)
        if serializer.is_valid():
            print("serializer is valid")
            serializer.save()
            return DRFResponse(serializer.data, status = status.HTTP_201_CREATED)
        return DRFResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(sel, request: DRFRequest, pk: int = None) -> DRFResponse:
        """
        Update an existing Ride objects.

        Args:
            request(Request) The HTTP request objects containing ride data.

        Returns:
            Response: Serialized Ride objects if updated or 40 if validation error.404 if not found 
        """
        try: 
            ride = Ride.objects.get(pk = pk)
        except Ride.DoesNotExist:
            return DRFResponse({"detail": "Not found."}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = RideSerializer(ride, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return DRFResponse(serializer.data)
        return DRFResponse(serializer.erors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(sel, request: DRFRequest, pk: int = None) -> DRFResponse:
        """
        Delete a Ride objects by pk.

        Args:
            request(Request) The HTTP request objects containing ride data.
            pk(int): Primary key of the Ride.

        Returns:
            Response: 204 No Content if deleted ,404 if not found 
        """
        try: 
            ride = Ride.objects.get(pk = pk)
        except Ride.DoesNotExist:
            return DRFResponse({"detail": "Not found."}, status = status.HTTP_404_NOT_FOUND)
        ride.delete()
        return DRFResponse(status = status.HTTP_204_NO_CONTENT)
    

class VehicleViewSet(ViewSet):
    """
    ViewSet for Vehicle model.

    Provides CRUD operations manually implemented with filtering, searching, and ordering.
    """

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["driver", "capacity"]
    search_fields = ["model", "license_plate"]
    ordering_fields = ["capacity"]

    def get_queryset(self) -> QuerySet:
        """
        Return the optimized queryset of Vehicle objects.

        Returns:
            QuerySet: Optimized queryset with select_related('driver').
        """
        return Vehicle.objects.select_related("driver").all()

    def list(self, request: DRFRequest) -> DRFResponse:
        """
        Return a list of Vehicle objects with optional filtering, searching, and ordering.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: List of serialized Vehicle objects.
        """
        vehicles = self.get_queryset()
        serializer = VehicleSerializer(vehicles, many=True)
        return DRFResponse(serializer.data)

    def retrieve(self, request: DRFRequest, pk: int = None) -> DRFResponse:
        """
        Retrieve a single Vehicle by primary key.

        Args:
            request (Request): The HTTP request object.
            pk (int): Primary key of the Vehicle.

        Returns:
            Response: Serialized Vehicle object or 404 if not found.
        """
        try:
            vehicle = self.get_queryset().get(pk=pk)
        except Vehicle.DoesNotExist:
            return DRFResponse({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = VehicleSerializer(vehicle)
        return DRFResponse(serializer.data)

    def create(self, request: DRFRequest) -> DRFResponse:
        """
        Create a new Vehicle object.

        Args:
            request (Request): The HTTP request object containing Vehicle data.

        Returns:
            Response: Serialized Vehicle object if created, 400 on validation error.
        """
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return DRFResponse(serializer.data, status=status.HTTP_201_CREATED)
        return DRFResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: DRFRequest, pk: int = None) -> DRFResponse:
        """
        Update an existing Vehicle object.

        Args:
            request (Request): The HTTP request object containing updated data.
            pk (int): Primary key of the Vehicle.

        Returns:
            Response: Serialized Vehicle object if updated, 400 on validation error, 404 if not found.
        """
        try:
            vehicle = self.get_queryset().get(pk=pk)
        except Vehicle.DoesNotExist:
            return DRFResponse({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return DRFResponse(serializer.data)
        return DRFResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: DRFRequest, pk: int = None) -> DRFResponse:
        """
        Delete a Vehicle object by primary key.

        Args:
            request (Request): The HTTP request object.
            pk (int): Primary key of the Vehicle.

        Returns:
            Response: 204 No Content if deleted, 404 if not found.
        """
        try:
            vehicle = self.get_queryset().get(pk=pk)
        except Vehicle.DoesNotExist:
            return DRFResponse({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        vehicle.delete()
        return DRFResponse(status=status.HTTP_204_NO_CONTENT)