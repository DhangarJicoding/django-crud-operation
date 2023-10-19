from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('insert/',views.insert,name='insert'),
    path('showpage/',views.showpage,name='showpage'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('update/<int:pk>',views.update,name='update'),
    path('deletedata/<int:pk>',views.deletedata,name='deletedata'),
]
