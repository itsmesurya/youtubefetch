class YTdataSerializer(serializers.ModelSerializer):

    class Meta:
        model = YTdata
        fields = ('id','title','search','created_at')