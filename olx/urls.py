"""olx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import VehicleProductView,VehicleProductDetailsView,VehicleReviewsView,VehicleReviewDetailsView,\
    VehiclePdViewsetView,VehiclePdModelViewsetView,VehicleReviewModelViewsetView,VehicleUsersView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/v1/products",VehiclePdViewsetView,basename="products")
router.register("api/v2/products",VehiclePdModelViewsetView,basename="vehicles")
router.register("api/v1/reviews",VehicleReviewModelViewsetView,basename="vreviews")
router.register("register",VehiclePdViewsetView,basename="myvcuser")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products",VehicleProductView.as_view()),
    path("products/<int:id>",VehicleProductDetailsView.as_view()),
    path("vreviews",VehicleReviewsView.as_view()),
    path("vreviews/<int:id>",VehicleReviewDetailsView.as_view())

]+router.urls
