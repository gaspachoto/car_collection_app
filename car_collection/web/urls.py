from django.urls import path, include

from car_collection.web.views import index, create_profile, edit_profile, delete_profile, details_profile, \
    catalogue, create_car, edit_car, delete_car, details_car

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalog'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('details/', details_profile, name='details profile'),
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('edit/<int:pk>/', edit_car, name='edit car'),
        path('delete/<int:pk>/', delete_car, name='delete car'),
        path('details/<int:pk>/', details_car, name='details car'),
    ])),
)