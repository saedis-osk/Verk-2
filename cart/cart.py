import datetime
from django.conf import settings
#from cart.models import Item
class ItemAlreadyExists(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        self.item_count = 0
        if not cart:
            cart = self.session[settings.CART_ID] = dict(pizza={}, drink={}, offer={})
        self.cart = cart
        self.save()

    #def __iter__(self):
    #    for p in self.cart.keys():
    #        self.cart[str(p)]['item'] = Item.objects.get(pk=p)

    def __len__(self):
        return sum(item['quantity'] for category in self.cart.values() for item in category.values())


    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def add(self, item):
        #print("CART ADD FUNC")
        #print(item)
        '''
        item_type = item['item_type']
        item_id = int(item['item_id'])
        item_name = item['name']
        item_desc = "lmao" #item['description']
        item_price = item['price']
        print(item_id)
        print(item_name)
        print(item_price)
        #print( item_id not in self.cart[item_type])
        if item_id not in self.cart[item_type]:
            self.cart[item_type][item_id] = {'name': item_name,
                                                     'quantity': 1,
                                                     'desc':item_desc,
                                                     'price':item_price}
        else:
            self.cart[item_type][item_id]['quantity'] += 1
        self.save()
        '''
        item_type = item['item_type']
        item_id = str(item['item_id'])
        item_name = item['name']
        item_desc = item['description']
        item_price = item['price']
        item_dict = self.cart[item_type].get(item_id, {})
        item_dict['name'] = item_name
        item_dict['desc'] = item_desc
        item_dict['price'] = item_price
        item_dict['quantity'] = item_dict.get('quantity', 0) + 1
        self.cart[item_type][item_id] = item_dict
        self.save()

    def remove(self, item_type, item_id):
        if item_id in self.cart[item_type]:
            del self.cart[item_type][item_id]
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = dict(pizza={}, drink={}, offer={})  # Clear the session cart
        self.session.modified = True  # Mark the session as modified

    def list(self):
        print(self.cart)