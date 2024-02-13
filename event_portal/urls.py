"""event_portal URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView

from api.views import *
from events.views import *
from accounts.views import *

import rest_framework



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/usersignup/', UserSignUpView.as_view(), name='user_signup'),
    path('accounts/organizersignup/', OrganizerSignUpForm.as_view(), name='organizer_signup'),
    path('accounts/profile/', user_profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('shopping_cart/delete_ticket/<pk>/', remove_single_ticket, name='remove_ticket'),
    path('shopping_cart/delete_tickets/<pk>/', remove_all_tickets, name='remove_all_tickets'),
    path('order_success', order_success, name='order_success'),
    path('search', search, name='search'),
    path('advances_search', advanced_search, name='advanced_search'),

    path('', index, name='index'),
    #path('event/create/', event_image_view, name='event_create'),
    path('event/create/', PersonCreateView.as_view(), name='event_create'),
    path('event/order1/', add_num_ticket, name='add_num_ticket'),
    path('event/new_date/<pk>/', AddEventCopyView.as_view(), name='add_event_copy'),
    path('event/category/<name>/', event_category1, name='event_category'),
    path('event/update/<pk>/', update_event, name='update_event'),
    path('event/update/date/<int:pk>/', update_event_date, name='update_event_date'),
    path('event/addcomment/', add_comment, name='add_comment'),
    path('event/<pk>/', event_detail, name='event_detail'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/events/', Events.as_view()),
    path('api/categories/', Categories.as_view()),
    path('api/eventdates/', EventDates.as_view()),
    path('api/organizers/', Organizers.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
