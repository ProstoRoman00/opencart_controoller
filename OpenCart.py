import requests
import json
import re

class OpenCart(object):
    api_key = ""
    api_token = ""
    user_name = "oc_Controller"
    status = 0
    url = ""
    products = {}
    categories = {}
    manufacturers = {}

    def connect(self, api_key, url):
        if self.status:
            raise Exception(
                'You already connceted!')
        if not api_key or not url:
            raise Exception("You haven't entered login data!")
        #response = requests.post("http://18world.ru/oc.php")
        #if response.text=="1":
        #    raise Exception('Program needs to be activated!')
        self.api_key = api_key
        self.url = url
        parameters = {'username': self.user_name, 'key': self.api_key}
        response = requests.post(url + "/index.php?route=api/login", data=parameters)
        post_response = json.loads(response.text)
        if not post_response:
            raise Exception('Error in connection to the server, please check the web address and API key!')
        if not post_response["api_token"]:
            raise Exception('Please, add your IP address into the white list in your shop administration panel!')
        self.api_token = post_response["api_token"]
        self.status = 1
        return self.status

    def get_url(self, code):
        return self.url + "/index.php?api_token=" + self.api_token + "&route=" + code

    def get_list(self):
        if self.status != 1:
            raise Exception('Unknown connection error!')
        response = requests.post(self.get_url("api/product"))
        list_products = json.loads(response.text)
        if len(list_products)!=1:
            self.products = list_products["products"]
            self.categories = list_products["categories"]
            self.manufacturers = list_products["manufacturers"]
        return len(self.products)

    def product_add(self, product):
        if self.status != 1:
            raise Exception('Unknown connection error!')
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(self.get_url("api/product/add"), data=product, headers=headers)
        encoded_json = json.loads(response.text)
        return len(self.products)

    def product_edit(self, product):
        if self.status != 1:
            raise Exception('Unknown connection error!')
        product=self.product_build_edition(product)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(self.get_url("api/product/edit"), data=product, headers=headers)
        encoded_json = json.loads(response.text)
        return len(self.products)

    def product_by_id(self, id):
        if self.status != 1:
            raise Exception('Unknown connection error!')
        response = requests.post(self.get_url("api/product/product"), data={'id': id})
        encoded_json = json.loads(response.text)
        return encoded_json

    def product_category(self, prod):
        for val in self.categories:
            if val.get(prod) is not None:
                return val.get(prod)
        return 0

    def product_id(self, prod):
        for val in self.products:
            if val["name"] == prod:
                return val["product_id"]
        return 0

    def product_manufecturer(self, prod):
        for val in self.manufacturers:
            if val.get(prod) is not None:
                return val.get(prod)
        return 0

    def product_build(self, prod, category):
        product = {}
        product.update({'product_description': {}})
        product.update({'product_category': "category"})
        product.update({'product_store': ['Default']})
        product["product_description"].update({'1': {}})
        product["product_description"]["1"].update({'name': prod[0]})
        product["product_description"]["1"].update({'description': ''})
        product["product_description"]["1"].update({'meta_title': prod[0]})
        product["product_description"]["1"].update({'meta_description': ''})
        product["product_description"]["1"].update({'meta_keyword': ''})
        product["product_description"]["1"].update({'tag': ''})
        try:
            product.update({'model': re.split(prod[1], prod[0], flags=re.IGNORECASE)[1]})
        except:
            product.update({'model': prod[0]})
        product.update({'sku': ''})
        product.update({'upc': ''})
        product.update({'ean': ''})
        product.update({'jan': ''})
        product.update({'isbn': ''})
        product.update({'mpn': ''})
        product.update({'location': ''})
        product.update({'price': prod[2]})
        product.update({'tax_class_id': '0'})
        product.update({'minimum': '1'})
        product.update({'subtract': '1'})
        product.update({'quantity': prod[3]})
        if int(prod[3]) > 0:
            product.update({'stock_status_id': '7'})
        else:
            product.update({'stock_status_id': '5'})
        product.update({'shipping': '1'})
        product.update({'date_available': '2020-07-11'})
        product.update({'length': ''})
        product.update({'width': ''})
        product.update({'height': ''})
        product.update({'length_class_id': '1'})
        product.update({'weight': ''})
        product.update({'weight_class_id': '1'})
        product.update({'status': '1'})
        product.update({'sort_order': '1'})
        product.update({'manufacturer': '0'})
        product.update({'manufacturer_id': self.product_manufecturer(prod[1])})
        product.update({'filter': ''})
        product.update({'download': ''})
        product.update({'related': ''})
        product.update({'option': ''})
        product.update({'image': ''})
        product.update({'points': ''})
        return json.dumps(product)

    def product_build_edition(self, prod):
        product = {}
        product.update({'product_id': prod["product_id"]})
        product.update({'product_description': {}})
        product.update({'product_store': ['Default']})
        product["product_description"].update({'1': {}})
        product["product_description"]["1"].update({'name': prod["name"]})
        product["product_description"]["1"].update({'description': prod["description"]})
        product["product_description"]["1"].update({'meta_title': prod["meta_title"]})
        product["product_description"]["1"].update({'meta_description': prod["meta_description"]})
        product["product_description"]["1"].update({'meta_keyword': prod["meta_keyword"]})
        product["product_description"]["1"].update({'tag': prod["tag"]})
        product.update({'model': prod["model"]})
        product.update({'sku': prod["sku"]})
        product.update({'upc': prod["upc"]})
        product.update({'ean': prod["ean"]})
        product.update({'jan': prod["jan"]})
        product.update({'isbn': prod["isbn"]})
        product.update({'mpn': prod["mpn"]})
        product.update({'location': prod["location"]})
        product.update({'price': prod["price"]})
        product.update({'tax_class_id': prod["tax_class_id"]})
        product.update({'minimum': prod["minimum"]})
        product.update({'subtract': prod["subtract"]})
        product.update({'quantity': prod["quantity"]})
        if int(prod["quantity"]) > 0:
            product.update({'stock_status_id': '7'})
        else:
            product.update({'stock_status_id': '5'})
        product.update({'date_available': prod["date_available"]})
        product.update({'length': prod["length"]})
        product.update({'width': prod["width"]})
        product.update({'height': prod["height"]})
        product.update({'length_class_id': prod["length_class_id"]})
        product.update({'weight': prod["weight"]})
        product.update({'weight_class_id': prod["weight_class_id"]})
        product.update({'status': prod["status"]})
        product.update({'sort_order': prod["sort_order"]})
        product.update({'manufacturer': prod["manufacturer"]})
        product.update({'manufacturer_id': prod["manufacturer_id"]})
        product.update({'points': prod["points"]})
        return json.dumps(product)