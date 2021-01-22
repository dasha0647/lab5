from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from MainApp.models import Product, Order, Locality, Client, Backup_copy, User
from MainApp.forms import FormProduct, FormOrder, FormUser, FormClient, FormBackup_copy, FormLocality
from MainApp import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='accounts/login/')),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('home/', views.index, name='home'),

    # product
    path('home/product/', views.index_product, name='product'),
    path('home/product/add/', views.view_product.add_product, name='add_product'),
    path('home/product/del/', views.view_product.del_product, name='del_product'),
    path('home/product/update/', views.view_product.update_product, name='update_product'),

    # order
    path('home/order/', views.index_order, name='order'),
    path('home/order/add/', views.view_order.add_order, name='add_order'),
    path('home/order/del/', views.view_order.del_order, name='del_order'),
    path('home/order/update/', views.view_order.update_order, name='update_order'),

    # locality
    path('home/locality/', views.index_locality, name='locality'),
    path('home/locality/add/', views.view_locality.add_locality, name='add_locality'),
    path('home/locality/del/', views.view_locality.del_locality, name='del_locality'),
    path('home/locality/update/', views.view_locality.update_locality, name='update_locality'),

    # client
    path('home/client/', views.index_client, name='client'),
    path('home/client/add/', views.view_client.add_client, name='add_client'),
    path('home/client/del/', views.view_client.del_client, name='del_client'),
    path('home/client/update/', views.view_client.update_client, name='update_client'),

    # backup_copy
    path('home/backup_copy/', views.index_backup_copy, name='backup_copy'),
    path('home/backup_copy/add/', views.view_backup_copy.add_backup_copy, name='add_backup_copy'),
    path('home/backup_copy/del/', views.view_backup_copy.del_backup_copy, name='del_backup_copy'),
    path('home/backup_copy/update/', views.view_backup_copy.update_backup_copy, name='update_backup_copy'),

    # user
    path('home/user/', views.index_user, name='user'),
    path('home/user/add/', views.view_user.add_user, name='add_user'),
    path('home/user/del/', views.view_user.del_user, name='del_user'),
    path('home/user/update/', views.view_user.update_user, name='update_user'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]