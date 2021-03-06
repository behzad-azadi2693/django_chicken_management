from django.urls import path

from farms.models import Losses
from .views import (
            farms, create_farm, edit_farm, profilechicken,
            create_profilechicken,edit_profilechicken,vaccinations,
            create_vaccination,edit_vaccination,manufacturing_farm,create_manufacturing,
            edit_manufacturing,farm, create_losse, edit_losse, losse, losses,
            incaomes, create_incaome, edit_incaome, functions, edit_function, 
            create_function, create_manage, edit_manage, schedules, create_schedule,
            edit_schedule, make_bery, create_make_bery, edit_make_bery, medicians, 
            create_medician, edit_medician, add_image_to_medician, all_image_medician,
            remove_image_medician, labratores, create_labratore, edit_labratore,
            remove_image_labratore, add_image_to_labratore, all_image_labratore,
        )

app_name = 'farms'

urlpatterns = [
    path('', farms, name='farms'),
    path('<int:pk>/', farm, name='farm'),
    path('create/farm/', create_farm, name='create_farm'),
    path('edit/farm/<int:pk>/', edit_farm, name='edit_farm'),
    path('profilechicken/<int:pk>/', profilechicken, name='profilechicken'),
    path('create/profilechicken/<int:pk>/', create_profilechicken, name='create_profilechicken'),
    path('edit/profilechicken/<int:pk>/', edit_profilechicken, name='edit_profilechicken'),
    path('vaccinations/<int:pk>/', vaccinations, name='vaccinations'),
    path('create/vaccination/<int:pk>/', create_vaccination, name='create_vaccination'),
    path('edit/vaccination/<int:pk>/', edit_vaccination, name='edit_vaccination'),
    path('manufacturing/all/<int:pk>/', manufacturing_farm, name='manufacturing_farm'),
    path('create/manufacturing/<int:pk>/', create_manufacturing, name='create_manufacturing'),
    path('edit/manufacturing/<int:pk>/', edit_manufacturing, name='edit_manufacturing'),
    path('edit/losse/<int:pk>/', edit_losse, name='edit_losse'),
    path('create/losse/<int:pk>/', create_losse, name='create_losse'),
    path('losse/<int:pk>/', losse, name='losse'),
    path('losses/<int:pk>/', losses, name='losses'),
    path('edit/incaome/<int:pk>/', edit_incaome, name='edit_incaome'),
    path('create/incaome/<int:pk>/', create_incaome, name='create_incaome'),
    path('incaomes/<int:pk>/', incaomes, name='incaomes'),
    path('edit/function/<int:pk>/', edit_function, name='edit_function'),
    path('create/function/<int:pk>/', create_function, name='create_function'),
    path('functions/<int:pk>/', functions, name='functions'),
    path('create/manage/<int:pk>/', create_manage, name='create_manage'),
    path('edit/manage/<int:pk>/', edit_manage, name='edit_manage'),
    path('edit/schedule/<int:pk>/', edit_schedule, name='edit_schedule'),
    path('create/schedule/<int:pk>/', create_schedule, name='create_schedule'),
    path('schedule/<int:pk>/', schedules, name='schedules'),
    path('make_bery/<int:pk>/', make_bery, name='make_bery'),
    path('create/make_bery/<int:pk>/', create_make_bery, name='create_make_bery'),
    path('edit/make_bery/<int:pk>/', edit_make_bery, name='edit_make_bery'),
    path('medicians/<int:pk>/', medicians, name='medicians'),
    path('create/medician/<int:pk>/', create_medician, name='create_medician'),
    path('edit/medician/<int:pk>/', edit_medician, name='edit_medician'),
    path('add/image_to_medician/<int:pk>/', add_image_to_medician, name='add_image_to_medician'),
    path('all/image_medician/<int:pk>/', all_image_medician, name='all_image_medician'),
    path('remove/image_medician/<int:pk>/', remove_image_medician, name='remove_image_medician'),
    path('labratores/<int:pk>/', labratores, name='labratores'),
    path('create/labratore/<int:pk>/', create_labratore, name='create_labratore'),
    path('edit/labratore/<int:pk>/', edit_labratore, name='edit_labratore'),
    path('add/image_to_labratore/<int:pk>/', add_image_to_labratore, name='add_image_to_labratore'),
    path('all/image_labratore/<int:pk>/', all_image_labratore, name='all_image_labratore'),
    path('remove/image_labratore/<int:pk>/', remove_image_labratore, name='remove_image_labratore'),
]
