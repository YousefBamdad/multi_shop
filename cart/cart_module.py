from product.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            product = Product.objects.get(id=int(item['id']))
            item['product'] = product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_id_generator(product.id, item['size'], item['color'])
            yield item

    def unique_id_generator(self, id, size, color):
        result = f"{id}-{size}-{color}"
        return result

    def remove_cart(self):
        del self.session[CART_SESSION_ID]

    def total(self):
        cart = self.cart.values()
        total = sum(int(item['quantity']) * int(item['price']) for item in cart)
        # for item in cart:
        #     total += int(item['quantity']) * int(item['price'])
        return total

    def add(self, product, quantity, size, color):

        unique = self.unique_id_generator(product.id, size, color)
        if unique not in self.cart:
            self.cart[unique] = {'quantity': 0, 'price': str(product.price), 'color': color, 'size': size,
                                 'id': str(product.id)}
        self.cart[unique]['quantity'] += int(quantity)
        self.save()

    def remove(self, unique_id):
        if unique_id in self.cart:
            del self.cart[unique_id]
            self.save()

    def save(self):
        self.session.modified = True
