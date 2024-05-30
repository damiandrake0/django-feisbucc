from django.urls import path

from . import views

urlpatterns = [
    path('',views.feisbucc,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('addPost/',views.add_post,name='addPost'),
    path('profile/<profile_id>',views.profileV,name='profile'),
    path('editProfile/<profile_id>',views.edit_profile,name='editProfile'),
    path('like/<id_post>',views.like,name='like'),
    path('profile/follow/<profile_id>',views.following,name='follow')#,
    # path('remlike/<id_post>',views.remlike,name='remlike')
]