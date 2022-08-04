"""celebrity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from apis import views
from rest_framework_swagger.views import get_swagger_view

from apis import views
schema_view = get_swagger_view(title='Users API')
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)  


urlpatterns = [
    # apis
    path('celebrity/',views.celebrity_data),
    path('celebrity/<str:id>',views.celebrity_single_data),
    path('Booking/',views.celebrity_bookings),
    # path('author/',views.AuthorlistView.as_view()),
    # path('author/<int:pk>',views.AuthorDetailView.as_view()),
    # path('book/',views.BooklistView.as_view()),
    # path('book/<int:pk>',views.BookDetailView.as_view()),
# swaager and token
    path('swagger/', schema_view,),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
