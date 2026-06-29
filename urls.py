from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("create/", views.create_account, name="create_account"),

    path("all/", views.all_accounts, name="all_accounts"),

    path("get/", views.get_account, name="get_account"),

    path("deposit/", views.deposit, name="deposit"),

    path("withdraw/", views.withdraw, name="withdraw"),

    path("update/", views.update_account, name="update_account"),

    path("delete/", views.delete_account, name="delete_account"),

]