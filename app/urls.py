from django.urls import path

from app.views import shopping_cart, checkout, create_product, \
    update_product, login_view, logout_view, register_view, ForgotPasswordView, new_product, delete_product, \
    ActivateEmailView, IndexPage, ShopPage, product_details, contact_view

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('product-details/<int:product_id>', product_details, name='shop-details'),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('shopping-cart/', shopping_cart, name='shopping-cart'),
    path('contact/', contact_view, name='contact'),
    path('checkout/', checkout, name='checkout'),

    path('create-product/', create_product, name='create-product'),
    path('update-product/<int:product_id>', update_product, name='update-product'),

    #auth
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('new-product/', new_product, name='new-product'),
    path('delete-product/<int:product_id>', delete_product, name='delete_product'),
    path('active/<str:uid>/<str:token>', ActivateEmailView.as_view(), name='confirm-mail'),
]