
from rest_framework import routers
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

from product.views import *
from .views import  *
from orders.views import *
schema_view = get_swagger_view(title='docs for tests')


router = routers.DefaultRouter()

router.register(r'permissions/get', PermissionViewSet)
#router.register(r'roles/get', RoleViewSet)
#router.register(r'orders_items', OrderItemViewSet)

router.register(r'groups/create', PostGroupViewSet, basename='groups_create')
router.register(r'groups/get', GetGroupViewSet, basename='groups_get')
router.register(r'groups/change', PutGroupViewSet, basename='groups_change')
router.register(r'groups/delete', DeleteGroupViewSet, basename='groups_delete')

router.register(r'users/create', PostUserViewSet, basename='users_create')
router.register(r'users/get', GetUserViewSet, basename='users_get')
router.register(r'users/change', PutUserViewSet, basename='users_change')
router.register(r'users/delete', DeleteUserViewSet, basename='users_delete')

router.register(r'orders/create', PostOrderViewSet, basename='orders_create')
router.register(r'orders/get', GetOrderViewSet, basename='orders_get')
router.register(r'orders/change', PutOrderViewSet, basename='orders_change')
router.register(r'orders/delete', DeleteOrderViewSet, basename='orders_delete')
router.register(r'orders_items', OrderItemViewSet)

router.register(r'products/create', PostProductViewSet, basename='products_create')
router.register(r'products/get', GetProductViewSet, basename='products_get')
router.register(r'products/change', PutProductViewSet, basename='products_change')
router.register(r'products/delete', DeleteProductViewSet, basename='products_delete')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('export/', ExportAPIView.as_view()),
    path('chart/', ChartAPIView.as_view()),
    #path('login', login, name="login_view"),
    path('authentification/', include('dj_rest_auth.urls')),
    path('authentification/registration/',include('dj_rest_auth.registration.urls')),
    path('docs',schema_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
