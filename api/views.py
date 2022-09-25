from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Vehicles,VehicleReviews
from api.serializers import VehicleSerializer,VehicleReviewSerializer,VehicleUserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User


class VehicleProductView(APIView):
    def get(self,req,*args,**kwargs):
        res=Vehicles.objects.all()
        serializer=VehicleSerializer(res,many=True)
        return Response(data=serializer.data)



    # def post(self,req,*args,**kwargs):
    #     vname=req.data.get("name")
    #     vmodel=req.data.get("model")
    #     vcolor = req.data.get("color")
    #     vprice = req.data.get("price")
    #     vtransmission = req.data.get("transmission")
    #     Vehicles.objects.create(name=vname,model=vmodel,color=vcolor,price=vprice,transmission=vtransmission)
    #     return Response(data="created")

    def post(self, req, *args, **kwargs):
        serializer = VehicleSerializer(data=req.data)
        if serializer.is_valid():
            Vehicles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



class VehicleProductDetailsView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        vehicle= Vehicles.objects.get(id=id)
        serializer = VehicleSerializer(vehicle, many=False)
        return Response(data=serializer.data)

    def delete(self, req, *args, **kwargs):
        id = kwargs.get("id")
        Vehicles.objects.get(id=id).delete()
        return Response(data="Deleted")

    def put(self, req, *args, **kwargs):
        id = kwargs.get("id")
        serializer = VehicleSerializer(data=req.data)
        if serializer.is_valid():
            Vehicles.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)




class VehicleReviewsView(APIView):

    def get(self,req,*args,**kwargs):
        reviews =VehicleReviews.objects.all()
        serializer = VehicleReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

    def post(self,req,*args,**kwargs):
        serializer = VehicleReviewSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



class VehicleReviewDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        qs = VehicleReviews.objects.get(id=id)
        serializer = VehicleReviewSerializer(qs, many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        object = VehicleReviews.objects.get(id=id)
        serializer = VehicleReviewSerializer(instance=object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        VehicleReviews.objects.get(id=id).delete()
        return Response(data="deleted")






class VehiclePdViewsetView(ViewSet):

    def list(self,req,*args,**kwargs):
        qs=Vehicles.objects.all()
        serializer=VehicleSerializer(qs,many=True)
        return Response(data=serializer.data)


    def create(self,req,*args,**kwargs):
        serializer=VehicleSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



    def retrieve(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        book=Vehicles.objects.get(id=id)
        serializer=VehicleSerializer(book,many=False)
        return Response(data=serializer.data)



    def update(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        book=Vehicles.objects.filter(id=id)
        serializer=VehicleSerializer(instance=book,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



    def destroy(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        Vehicles.objects.get(id=id).delete()
        return Response(data="deleted")






class VehiclePdModelViewsetView(ModelViewSet):
    serializer_class=VehicleSerializer
    queryset = Vehicles.objects.all()


class VehicleReviewModelViewsetView(ModelViewSet):
    serializer_class = VehicleReviewSerializer
    queryset = VehicleReviews.objects.all()
    def list(self, request, *args, **kwargs):
        allreviews=VehicleReviews.objects.all()
        if "user" in request.query_params:
            allreviews=allreviews.filter(user=request.query_params.get("user"))
        serializer = VehicleReviewSerializer(allreviews, many=True)
        return Response(data=serializer.data)




class VehicleUsersView(ModelViewSet):
    serializer_class = VehicleUserSerializer
    queryset = User.objects.all()