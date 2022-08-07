from django.shortcuts import render, HttpResponse, redirect
from .models import QrCodes, Viewed_Qr_code, Viewer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
  if not request.user.is_authenticated:
    return redirect("/login")

  qr_code=QrCodes.objects.all()
  print(qr_code.reverse())
  return render(request, "main/index.html", {'qr_code':qr_code} )


def create_qr_code(request):
  if not request.user.is_authenticated:
    return redirect("/login")

  params= {
    "msg": ""
  }

  if request.method=="POST":
      stall_name = request.POST['stall_name']
      stall_location = request.POST['stall_location']

      QrCodes.objects.create(
        stall_name=stall_name,
        stall_location=stall_location
      )

      params['msg'] = "Created Qr code successfully"

  return render(request, "main/createqrcodes.html", params)


def viewer_list(request):

  data = Viewer.objects.order_by('-coins')
  params = {'data' : data}

  return render(request, "main/viewer_list.html", params)

def check_if_qr_code_valid(qr_uuid):
  data = QrCodes.objects.filter(uuid = qr_uuid)

  if len(data) > 0:
    return data, True
  else:
    return None, False

def user_check(username, password):
  data = Viewer.objects.filter(name = username, password = password)

  if len(data) > 0:
    return data, True
  else:
    return None, False

@api_view(['POST'])
def add_coin(request):
  username = request.data["username"]
  password = request.data["password"]
  uuid = request.data['uuid']

  qr_data, bool_check_qr = check_if_qr_code_valid(uuid)
  user_data, bool_check_user = user_check(username, password)

  if bool_check_qr and bool_check_user:
    qr_data = qr_data[0]
    user_data = user_data[0]

    coin_check = Viewed_Qr_code.objects.filter(viewer = user_data, qr_code = qr_data)

    if len(coin_check) > 0:
      return Response({
        "msg": "failed",
      })
    else:
      user_data.coins += 1
      user_data.save()
      Viewed_Qr_code.objects.create(viewer = user_data, qr_code = qr_data)

    return Response({
      "msg": "done",
    })
  else:
    return Response({
      "msg": "failed",
    })

@api_view(["POST"])
def signup(request):
  username = request.data["username"]
  password = request.data["password"]

  user_check = Viewer.objects.filter(name = username)

  if len(user_check) > 0:
    return Response({
      "msg": "userex",
    })

  coins = 0

  data = Viewer.objects.create(
    name = username,
    password = password,
    coins = 0
  )

  return Response({
    "msg": "done"
  })


@api_view(["POST"])
def login(request):
  check = Viewer.objects.filter(name = request.data["username"], password = request.data["password"])

  if len(check) > 0:
    return Response({
      "msg": "login"
    })

  return Response({
    "msg": "login failed"
  })

  
# {'username': 'tester1', 'password': 'test1234', 'uuid': 'a1eeae3f-7140-4f2d-a746-bc08238820de'}