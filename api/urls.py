from django.urls import path
from .views import *

urlpatterns = [
  path("", index, name="index"),
  path("create_qr_code/", create_qr_code, name="create_qr_code"),
  path("api/coins/add/user", add_coin, name="add_coin"),
  path('api/user/signup', signup, name="signup"),
  path('api/user/login', login, name="login"),
  path("viewer_list/", viewer_list, name="viewer_list"),
  path('api/user/coins', get_coins_data, name="get_coins_data"),
]