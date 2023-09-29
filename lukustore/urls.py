from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # Admin
    path("admin/", admin.site.urls),

    # Home page
    path('', index, name='index'),

    # <---- Shop/Store - All products in store
    path('shop/', shop, name='shop'),

    # <---- All Blogs
    path('blog/', blog_list, name='blog_list'),

    # ----> Single Blog View
    path('blog/<str:pk>/', blog_detail, name='blog_detail'),

    # Edit blog
    path('edit_blog/<int:id>/', edit_blog, name='edit_blog'),

    # New Blog
    path('add_blog/', add_blog, name='add_blog'),

    # About Us
    path('lukufam/', lukufam, name='lukufam'),

    # Account
    path('account/', account, name='account'),

    # Login
    path('login/', loginPage, name='login'),

    # Logout
    path('logout/', logoutUser, name='logout'),

    # Register User
    path('register/', registerPage, name='register'),

    # Error 404 Page
    path('error/', error, name='error'),

    # <---- Cart view
    path('cart/', cart, name='cart'),

    # ----- Cart view
    path('confirmed/', confirmed, name='confirmed'),

    # ----> Checkout view
    path('checkout/', checkout, name='checkout'),

    # Newsletter
    path('newsletter/', newsletter, name='newsletter'),

    # Help
    path('help/', help, name='help'),

    # Updates the item to the backend
    path('updateItem/', updateItem, name='updateItem'),

    # Processes the data in the backend
    path('processOrder/', processOrder, name='processOrder'),

    # Adds a product to the database/inventory
    path('add/', add, name='add'),

    # Update Photo
    path('edit/<int:id>/', edit, name='edit'),

    # Music Mixes
    path('music/', music, name='music'),
    path('music/<int:id>/', music_player, name='music_player'),

    # Trials
    path('gallery/', gallery, name='gallery'),
    path('photo/<str:pk>/', viewPhoto, name='photo'),
    path('addphoto/', addPhoto, name='addphoto'),
    path('addphoto/', addPhoto, name='addphoto'),

    # Product Details
    path('details/<str:pk>/', product_detail, name='product_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
