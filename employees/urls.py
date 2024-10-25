from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet,CustomFieldViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)  # This should work if queryset is defined
router.register(r'custom-fields', CustomFieldViewSet, basename='customfield')

urlpatterns = [
    path('api/', include(router.urls)),
]
