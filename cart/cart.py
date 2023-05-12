import datetime
from django.conf import settings
from cart.models import Item
class ItemAlreadyExists(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['item'] = Item.objects.get(pk=p)

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def add(self, item_id, quantity=1, update_quantity=False):
        item_id = str(item_id)

        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 1, 'id': item_id}

        if update_quantity:
            self.cart[item_id]['quantity'] += int(quantity)

            if self.cart[item_id]['quantity'] == 0:
                self.remove(item_id)
        self.save()

    def remove(self, item_id):
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}  # Clear the session cart
        self.session.modified = True  # Mark the session as modified
