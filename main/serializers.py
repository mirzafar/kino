from rest_framework import serializers

class DirectorSerializer(serializers.Serializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    status = serializers.IntegerField()


class ActorSerializer(serializers.Serializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    status = serializers.IntegerField()


class WriterSerializer(serializers.Serializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    status = serializers.IntegerField()


class GenreSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()   


class FilmSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    create_date = serializers.DateTimeField()
    age_limit = serializers.IntegerField()
    directors = DirectorSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)   
    writers = WriterSerializer(read_only=True, many=True) 
    genres = GenreSerializer(read_only=True, many=True)



