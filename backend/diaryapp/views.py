from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Entry, Diary, User, SignInDetail, Locker, Memo 
from .serializers import EntrySerializer, DiarySerializer, UserSerializer, SignInDetailSerializer, LockerSerializer, MemoSerializer, SignUpSerializer, LoginSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SignInDetail
from .serializers import SignInDetailSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import CustomAuthTokenSerializer  # Ensure to import your custom serializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    # permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignInDetailViewSet(viewsets.ModelViewSet):
    queryset = SignInDetail.objects.all()
    serializer_class = SignInDetailSerializer

class LockerViewSet(viewsets.ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer

class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

class CreateUserAPIView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            signin_detail = serializer.save()
            
            user = User.objects.create(
                email=signin_detail,
                username=signin_detail.email, 
                eyeColour='Unknown',  
                hairColour='Unknown'  
            )
            
            return Response({
                "user_id": user.userId,
                "email": signin_detail.email,
                "username": user.username,
                "eye_colour": user.eyeColour,
                "hair_colour": user.hairColour
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            try:
                signin_detail = SignInDetail.objects.get(email=email)
                if check_password(password, signin_detail.password):
                    user = User.objects.get(email=signin_detail)
                    print('User authenticated successfully')
                    return Response({
                        'user_id': user.userId,
                        'email': user.email.email,
                        'username': user.username
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            except SignInDetail.DoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutUserAPIView(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer  # Use your custom serializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
# class CurrentUserDetailView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         # Assuming the email is unique and matches the logged-in user
#         sign_in_detail = SignInDetail.objects.get(email=request.user.email)
#         serializer = SignInDetailSerializer(sign_in_detail)
#         return Response(serializer.data)  # This will now return only the email
    

# class EntryListCreate(APIView):
#     def get(self, request):
#         entries = Entry.objects.all()
#         serializer = EntrySerializer(entries, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EntrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EntryDetail(APIView):
#     def get(self, request, pk):
#         try:
#             entry = Entry.objects.get(pk=pk)
#             serializer = EntrySerializer(entry)
#             return Response(serializer.data)
#         except Entry.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

# def CreateMemo(self,User,Crush):

#     f
#     name=User.name
#     eyeColour=User.eyeColour
#     hairColour=User.hairColour
#     Crush.matching