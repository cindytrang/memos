from rest_framework import serializers
from .models import User, Diary, Entry, SignInDetail, Locker, Memo 
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth.hashers import make_password
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SignInDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignInDetail
        fields = '__all__'

class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker
        fields = '__all__'

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'

class CustomAuthTokenSerializer(AuthTokenSerializer):
    # You can customize your serializer here if needed
    pass

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignInDetail
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return SignInDetail.objects.create(**validated_data)