from django.db.models import Sum,F,Min,FloatField

from postings.models import BlogPost

from rest_framework import serializers, pagination




class BlogPostSerializer(serializers.ModelSerializer): # forms.ModelForm

    cpi = serializers.SerializerMethodField(method_name='calculate_cpi',read_only=True)

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(BlogPostSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = BlogPost
        fields = [
            'channel',
            'date',
            'country',
            'os',
            'impressions',
            'clicks',
            'installs',
            'spend',
            'revenue',
            'cpi',
        ]



    def calculate_cpi(self,obj):
        return obj.cpi


    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value
