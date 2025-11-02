import re
from rest_framework import serializers
from .models import Mockup, Result


class MockupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mockup
        fields = '__all__'
        read_only_fields = ['task_id', 'created_at', 'user']
    

    def validate_text_color(self, value):

        value = value.strip().upper()
        if not re.fullmatch(r'#([0-9A-F]{3}|[0-9A-F]{6})', value):
            raise serializers.ValidationError("Color must be a valid HEX code (#RGB or #RRGGBB), e.g. #FFF or #FFFFFF.")
        return value
    
    def validate_shirt_colors(self, value):

        # check it’s a list
        if not isinstance(value, list):
            raise serializers.ValidationError("shirt_colors must be a list.")

        # check unique items
        if len(set(value)) != len(value):
            raise serializers.ValidationError("Don't repeat shirt colors.")

        # check all items are valid
        allowed_colors = {choice[0] for choice in Mockup.SHIRT_COLOR_CHOICES}
        invalid_colors = [c for c in value if c not in allowed_colors]
        if invalid_colors:
            raise serializers.ValidationError(
                f"Invalid color(s): {', '.join(invalid_colors)}. Allowed: {', '.join(allowed_colors)}."
            )

        return value
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


class ResultSerializer(serializers.ModelSerializer):
    mockup_task_id = serializers.UUIDField(source='mockup.task_id', read_only=True)

    class Meta:
        model = Result
        fields = ['mockup_task_id', 'image_url', 'created_at']
        read_only_fields = ['created_at', 'mockup_task_id']