from django.forms import widgets
from rest_framework import serializers
from mixincla.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=False,
    #                               max_length=100)
    # code = serializers.CharField(max_length=100000)
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
    #                                    default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES,
    #                                 default='friendly')
    class Meta:
        model= Snippet
        fields = ("__all__")



