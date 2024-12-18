from django.urls import path

from . import views

urlpatterns = [
    path("", views.check_article, name="check_article"),
    path("register/", views.RegisterView, name="register"),
    path("login/", views.LoginView, name="login"),
    path("logout/", views.LogoutView, name="logout"),
    path("forgot-password/", views.ForgotPassword, name="forgot-password"),
    path(
        "password-reset-sent/<str:reset_id>/",
        views.PasswordResetSent,
        name="password-reset-sent",
    ),
    path("reset-password/<str:reset_id>/", views.ResetPassword, name="reset-password"),
    path('check-abstract/', views.check_article, name='check_article'),
    path('result/', views.result, name="result")
]

