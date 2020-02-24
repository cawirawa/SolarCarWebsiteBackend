from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, BasePermission
from .permissions import IsAdminOrReadOnly
from .models import OurTeam, TeamPage, NavBar, Photo
from django.contrib.auth.models import User
from .serializer import OurTeamSerializer, UserSerializer, TeamPageSerializer, NavBarSerializer, PhotoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminOrReadOnly, )

    # to create a new user
    @action(detail=False, methods=['POST'])
    def update_user(self, request, pk=None):
        # check if 'first_name', 'last_name', 'email' is provided.
        if 'first_name' in request.data and 'last_name' in request.data and 'email' in request.data:
            is_staff = False
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']

            # if 'is_staff' is provided in the request
            if 'is_staff' in request.data:
                is_staff = request.data['is_staff']

            # if user existed
            try:
                obj = User.objects.get(email=email)
                if 'is_staff' in request.data:
                    obj.is_staff = is_staff
                obj.first_name = first_name
                obj.last_name = last_name
                obj.save()
                serializer = UserSerializer(obj, many=False)
                response = {'message': 'User updated', 'result': serializer.data }
                return Response(response, status=status.HTTP_200_OK)
           
            # create new user
            except User.DoesNotExist:
                obj = User.objects.create(first_name=first_name, last_name=last_name, email = email, is_staff=is_staff, username=email)
                Token.objects.create(user=obj)
                serializer = UserSerializer(obj, many=False)
                response = {'message': 'New user created.', 'result': serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)
        
        # If user details are not provided
        else:
            response = {'message': 'Please provide \'first_name\', \'last_name\', and \'email\''}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class OurTeamViewSet(viewsets.ModelViewSet):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer 
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminOrReadOnly,)

    @action(detail=False, methods=['POST'])
    def update_our_team(self, request, pk=None):
        if 'full_name' in request.data and 'bio' in request.data and 'profile_image' in request.data:
            full_name = request.data['full_name']
            bio = request.data['bio']
            profile_image = request.data['profile_image']
            if 'profile_header' in request.data:
                profile_header = request.data['profile_header']
            else:
                profile_header = ""
            if 'user_email' in request.data:
                email = request.data['user_email']
            else:
                email = "default@ucsd.edu"
            if 'bio2' in request.data:
                bio2 = request.data['bio2']
            else:
                bio2 = ""
            if 'cropping' in request.data:
                cropping = request.data['cropping']
            else:
                cropping = "144x144"
            try:
                user = User.objects.get(email=email)
                obj = OurTeam.objects.get(user=user)
                obj.full_name = full_name
                obj.profile_image = profile_image
                obj.bio = bio
                obj.bio2 = bio2
                obj.save()
                serializer = OurTeamSerializer(obj, many=False)
                response = {'message': 'Successfully updated our team chart', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)           
            except User.DoesNotExist:
                response = {'message': 'User does not exist!'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            except OurTeam.DoesNotExist :
                obj = OurTeam.objects.create(full_name=full_name, bio=bio, bio2=bio2, user=user, profile_header=profile_header, profile_image=profile_image, cropping=cropping)
                serializer = OurTeamSerializer(obj, many=False)
                response = {'message': 'New team created.', 'result': serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)
            
        else:
            response = {'message': 'Please provide \'full_name\', \'bio\', and \'user_email\''}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class TeamPageViewSet(viewsets.ModelViewSet):
    queryset = TeamPage.objects.all()
    serializer_class = TeamPageSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminOrReadOnly, )

    @action(detail=False, methods=['POST'])
    def update_team_page(self, request, pk=None):
        if 'header' in request.data and 'content' in request.data:
            header = request.data['header']
            content = request.data['content']
            obj = TeamPage.objects.get(id=1)
            obj.header = header
            obj.content = content
            obj.save()
            serializer = TeamPageSerializer(obj, many=False)
            response = {'message': 'Successfully updated our team page', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)    
        else:
            response = {'message': 'Please provide \'header\', and \'content\''}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class NavbarViewSet(viewsets.ModelViewSet):
    queryset = NavBar.objects.all()
    serializer_class = NavBarSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminOrReadOnly, )

    @action(detail=False, methods=['POST'])
    def update_navbar(self, request, pk=None):
        # check if 'first_name', 'last_name', 'email' is provided.
        if 'name' in request.data and 'link' in request.data:
            name = request.data['name']
            link = request.data['link']

            # if button existed
            try:
                obj = NavBar.objects.get(name=name)
                obj.name = name
                obj.link = link
                obj.save()
                serializer = NavBarSerializer(obj, many=False)
                response = {'message': 'Button updated', 'result': serializer.data }
                return Response(response, status=status.HTTP_200_OK)
           
            # create new user
            except NavBar.DoesNotExist:
                obj = NavBar.objects.create(name=name, link=link)
                serializer = NavBarSerializer(obj, many=False)
                response = {'message': 'New button created.', 'result': serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)
        
        # If button details are not provided
        else:
            response = {'message': 'Please provide \'name\', and \'link\''}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminOrReadOnly, )

    @action(detail=False, methods=['POST'])
    def update_photo(self, request, pk=None):
        # check if 'first_name', 'last_name', 'email' is provided.
        if 'name' in request.data and 'image' in request.data:
            name = request.data['name']
            image = request.data['image']

            # if photo existed
            try:
                obj = NavBar.objects.get(name=name)
                obj.name = name
                obj.image = image
                obj.save()
                serializer = PhotoSerializer(obj, many=False)
                response = {'message': 'Photo updated', 'result': serializer.data }
                return Response(response, status=status.HTTP_200_OK)
           
            # create new photo
            except NavBar.DoesNotExist:
                obj = NavBar.objects.create(name=name, image=image)
                serializer = PhotoSerializer(obj, many=False)
                response = {'message': 'New photo created.', 'result': serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)
        
        # If photo details are not provided
        else:
            response = {'message': 'Please provide \'name\', and \'image\''}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

