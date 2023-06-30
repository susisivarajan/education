from .import views
from django.urls import path


urlpatterns=[

    path("",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("login/",views.login_form,name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("app", views.application_form, name="app"),
    path("ba/", views.ba, name="ba"),
    path("bsc/", views.bsc, name="bsc"),
    path("commerce/", views.commerce, name="commerce"),
    path("bed/", views.bed, name="bed"),
    path("computer/", views.computer, name="computer"),
    path("new/", views.new, name="new"),
    path("success/", views.success, name="success"),

]
