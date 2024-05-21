from django.urls import path
from.import views
urlpatterns = [
    path('',views.Userlogin,name='Userlogin'),
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('addtask/',views.addtask,name='addtask'),
    path('viewtask/',views.viewtask,name='viewtask'),
    path('edittask/<int:task_id>',views.edittask,name='edittask'),
    path('deletetask/<int:task_id>',views.deletetask,name='deletetask'),
    path('logout/', views.UserLogout, name='logout'),

]