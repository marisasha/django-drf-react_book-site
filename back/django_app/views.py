
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import QuerySet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from django_app import models, serializers 



@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  
def api(request: Request) -> Response:
    return Response(
                    data={"message": "OK"},
                    status=200
                    )


@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])
def api_register(request: Request) -> Response:
    username = request.data.get("username", None)
    password = request.data.get("password", None)
    if username and password:
        User.objects.create(username=username, password=make_password(password))
        return Response(
                        data={"success": "Account succesfully created!"}, 
                        status=200
                        )
    else:
        return Response(
                        data={"error": "Login or password is incorrect"},   
                        status=401
                        )


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def api_book(request: Request) -> Response:
    try:
        if request.method == "GET":
            _obj = models.Book.objects.all()
            _json = serializers.BookSimpleSerializer(_obj, many=True if isinstance(_obj, QuerySet) else False).data
            return Response(
                            data={"succes":_json}
                            )
    except Exception as error:
        return Response(
                        data={"error": str(error)}, 
                        status=400
                        )


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def api_book_id(request: Request, book_id: str) -> Response:
    try:
        if request.method == "GET":
            _obj = models.Book.objects.get(id=int(book_id))
            _json = serializers.BookSimpleSerializer(_obj, many=True if isinstance(_obj, QuerySet) else False).data
            return Response(
                            data={"succes":_json}
                            )
    except Exception as error:
        return Response(
                        data={"error": str(error)}, 
                        status=400
                        )
