from rest_framework.views import APIView
from ..serializers.authSerializers import LoginSerializers,RegisterSerializers
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
User = get_user_model()

class Login(APIView):
    
    permission_classes = [AllowAny]
    
    http_method_names = ["post"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
    
    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
    def post(self,request,*args, **kwargs):
        user = LoginSerializers(data=request.data)
        
        if not user.is_valid():
            return Response("Invalid Data")
        
        login(request,user.validated_data)
        token = self.get_tokens_for_user(user.validated_data)
        
        return Response(token)
        
        
class Register(APIView):
    
    permission_classes = [AllowAny]
    
    http_method_names = ["post"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
    
    def post(self,request,*args, **kwargs):
        user = RegisterSerializers(data=request.data)
        
        if user.is_valid():
           try:
                user.save(password=make_password(request.data["password"]))
                return Response("User Register success")
           except Exception:
               return Response("Error")
        else:
            return Response(user.errors)
    


class Update(APIView):
    
    http_method_names = ["put"]
    
    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]
    
    def get_object(self):
        print(self.request.path_info)
        try:
            pk = self.kwargs["pk"]
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
    
    def update_password(self,serializers):
        newPassword = make_password(self.request.data["new-password"])
        serializers.save(password=newPassword)
    
    def put(self,request,*args, **kwargs):
        
        instanceOrNone = self.get_object()
        
        if instanceOrNone is None:
            return Response("User Do not exist")
        
        user = RegisterSerializers(instance=instanceOrNone,data=request.data,partial=True)
        
        if self.request.path.__contains__("password"):
            if 'original-password'  in request.data:
                if instanceOrNone.check_password(raw_password=request.data["original-password"]):
                    if user.is_valid():
                        self.update_password(user)
                    else:
                        return Response("Error")
                else:
                    return Response("Password Do not match")
            else:
                return Response("The old password is required")
            
        if user.is_valid():
           try:
                user.save()
                return Response("User Register success")
           except Exception:
               return Response("Error")