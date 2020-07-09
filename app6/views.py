from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
import json
from app6.forms import ProductForm
from app6.models import Product

class CreateOneProduct(View):
    def post(self,request):
        data = request.body # Reading data from consumer (data will be in binary string format)
        dict_data = json.loads(data) # Converting binary string into dict Format
        pf = ProductForm(dict_data) # Sending dict data to Form class
        if pf.is_valid():
            pf.save()
            json_da = json.dumps({"message":"Product is Saved"})
        else:
            json_da = json.dumps({"error":pf.errors})

        return HttpResponse(json_da,content_type="application/json")


class DeleteOneProduct(View):
    def get(self,request,productno):
        try:
            res = Product.objects.get(pno=productno)
            res.delete()
            json_data = json.dumps({"mesage":"Product is Deleted Succesfully"})
        except:
            json_data = json.dumps({"error":"Product No is Invalid"})

        return HttpResponse(json_data,content_type="application/json")


class UpdateOneProduct(View):
    def put(self,request,productno):
        try:
            old_product = Product.objects.get(pno=productno)
            data = request.body
            new_product = json.loads(data)
            pf = ProductForm(new_product, instance=old_product)
            if pf.is_valid():
                pf.save()
                json_data = json.dumps({"Message": "Product is updated"})
            else:
                json_data = json.dumps({"error": "Product no is Invalid"})
        except Product.DoesNotExist:
            json_data = json.dumps({"Error": "Invalid Product No"})

        return HttpResponse(json_data,content_type="application/json")