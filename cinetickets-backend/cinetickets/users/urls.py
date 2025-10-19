from django.urls import path
from .views import RegisterView, LoginView, SoftDeleteUserView, UserDetailView
from knox import views as knox_views

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
    path("me/", UserDetailView.as_view(), name="user-detail"),
    path("me/soft-delete/", SoftDeleteUserView.as_view(), name="user-soft-delete"),
]
