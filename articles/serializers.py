from rest_framework import serializers

class ArtilceSerializer(serializers.Serializer):

    title = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        max_length=20,
        error_messages={
            "invalid":"invalid title",
            "blank":"not blank",
            "max_length":"title is to long",

        }
    )

    email = serializers.EmailField()

    offest = serializers.IntegerField()

