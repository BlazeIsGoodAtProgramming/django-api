from rest_framework import serializers
from root.models import *




class Serviceserializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [ 'title' ]


class SpecialServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialService
        fields = [ 'title' , 'description']



class Teamserializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = [ 'name' , 'skill' , 'facebook' , 'twitter'  , 'linkedin']



class Testimonialserializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = [ 'name'  , 'description']



class Skillserializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = [ 'title' ]


class ContactUsserializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = [ 'name' , 'email' , 'subject' , 'message' ]

