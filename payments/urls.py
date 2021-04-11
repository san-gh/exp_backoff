from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:txn_id>/', views.viewTxn, name="viewTxn"),
    path('post/', views.postTxn, name="postTxn")
]