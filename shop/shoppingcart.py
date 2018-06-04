# -*- coding: utf-8 -*-

from decimal import Decimal
from django.conf import settings
from shop import models as shop_models

class ShoppingCart(object):

    def __init__(self, resquest):
        self.session = resquest.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    #def add(self, product, quantity=1, update_quantity=False):
    def add(self, product):
        product_id = str(product.id)
        if product.id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price': str(product.price)}
        """
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        """
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def remove(self, product):
        product_id = str(product.id)
        #if product.id in self.cart:
        del self.cart[product_id]
        self.save()

    def update(self, product, quantity):
        product_id = str(product.id)
        #shopingchart_form = shop_forms.ShoppingCartForm(request.POST)
        #if product.id in self.cart:
        self.cart[product_id] = {'quantity': 6, 'price': str(product.price)}


    def __iter__(self):
        product_ids = self.cart.keys()
        products = shop_models.Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['totalPrice'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def getTotalPrice(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
