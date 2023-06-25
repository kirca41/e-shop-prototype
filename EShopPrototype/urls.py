"""EShopPrototype URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products.views import index, register, add_product, categories, guitar_category, keyboard_category, \
    percussion_category, amplifiers_category, cables_category, shopping_cart, add_to_cart, place_order, \
    remove_from_shopping_cart, product_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('', index, name='index'),
    path('product_details/<int:product_id>', product_details, name='product_details'),
    path('add_product/', add_product, name='add_product'),
    path('categories/', categories, name='categories'),
    path('categories/guitars', guitar_category, name='guitar_category'),
    path('categories/keyboards', keyboard_category, name='keyboard_category'),
    path('categories/percussion', percussion_category, name='percussion_category'),
    path('categories/amplifiers', amplifiers_category, name='amplifiers_category'),
    path('categories/cables', cables_category, name='cables_category'),
    path('shopping_cart/', shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_shopping_cart, name='remove_from_shopping_cart'),
    path('checkout/', place_order, name='place_order'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
