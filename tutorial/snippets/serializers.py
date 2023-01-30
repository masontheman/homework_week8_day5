from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Video, Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self,validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ['id','username','email','password','first_name','last_name']
        
class VideoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Video
       fields = '__all__'
    #    fields = [user,title,thumb,video,views,likes,pub_date,desc]
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post     
        fields = '__all__' 
    # def create(self, validated_data) 
    # user = User.objects.get()