"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from myapp.views import ChavaView, HomeView, AboutView, Product_allView, Product_bowlView, Product_boxView, Product_cupView, Product_cutleryView, Product_plateView, Product_strawView, ContactView, DetailDetailView, BillView, CardView
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chava/', ChavaView.as_view(),name='chava'),
    path('home/',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about'),  
    path('product_all/',Product_allView.as_view(),name='productall'), 
    path('product_bowl/',Product_bowlView.as_view(),name='productbowl'), 
    path('product_box/',Product_boxView.as_view(),name='productbox'),
    path('product_cup/',Product_cupView.as_view(),name='productcup'), 
    path('product_cutlery/',Product_cutleryView.as_view(),name='productcutlery'), 
    path('product_straw/',Product_strawView.as_view(),name='productstraw'),
    path('product_plate/',Product_plateView.as_view(),name='productplate'),
    path('contact/',ContactView.as_view(),name='contact'), 
    path('detail/<int:pk>',DetailDetailView.as_view(),name='detail'), 
    path('bill/',BillView.as_view(),name='bill'),  
    path('card/',CardView.as_view(),name='card'), 

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    path('accounts/', include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)