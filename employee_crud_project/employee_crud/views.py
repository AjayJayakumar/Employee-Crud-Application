from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer


# Add details of new employee and get the list of employees
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Update the details of an existing employee
class RetrieveUpdateEmployeeDetails(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # Retrieve existing employee details
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # Update existing employee details
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Partial update of existing employee details
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# Delete the details of an existing employee
class DeleteEmployee(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
