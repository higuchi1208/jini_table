from django.urls import path
from . import views

urlpatterns = [
  path('', views.JiniList.as_view(), name="jinilist"),
  path('jinidelete/<int:pk>/', views.JiniDelete.as_view(), name="jinidelete"),
  path('jinicreate/', views.JiniCreate.as_view(), name="jinicreate"),

  path('companycreate/', views.CompanyCreate.as_view(), name="companycreate"),
  path('companydelete/<int:pk>/', views.CompanyDelete.as_view(), name="companydelete"),
  
]