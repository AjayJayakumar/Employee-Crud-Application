from django.urls import path
from .views import EmployeeList, RetrieveUpdateEmployeeDetails, DeleteEmployee

urlpatterns = [
    path("employee/", EmployeeList.as_view(), name="employee_details"),
    path(
        "employee/<int:pk>/",
        RetrieveUpdateEmployeeDetails.as_view(),
        name="retrieve-update_employee",
    ),
    path("delete-employee/<int:pk>/", DeleteEmployee.as_view(), name="delete_employee"),
]
