from decimal import Decimal
from .models import CartModel, CartItemModel
from shop.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.user = request.user
        cart = self.session.get('cart')
        if cart is None:
            cart = self.session['cart'] = {}
        self.cart = cart
        
        # If user is authenticated, sync with DB
        if self.user.is_authenticated:
            self.sync_with_db()

    def sync_with_db(self):
        # Get or create DB cart
        db_cart, created = CartModel.objects.get_or_create(user=self.user)
        
        # If session cart is empty but DB cart has items, load from DB
        if not self.cart and db_cart.items.exists():
            for item in db_cart.items.all():
                self.cart[str(item.product.id)] = {
                    'price': str(item.product.price),
                    'title': item.product.title,
                    'quantity': item.quantity
                }
            self.session.modified = True
        
        # If session cart has items, merge with DB
        elif self.cart:
            # Merge DB items into session if not present
            if db_cart.items.exists():
                for item in db_cart.items.all():
                    pid = str(item.product.id)
                    if pid not in self.cart:
                        self.cart[pid] = {
                            'price': str(item.product.price),
                            'title': item.product.title,
                            'quantity': item.quantity
                        }
                self.session.modified = True
            
            # Save combined state to DB
            self.save_to_db()

    def save_to_db(self):
        if self.user.is_authenticated:
            db_cart, _ = CartModel.objects.get_or_create(user=self.user)
            db_cart.items.all().delete()
            for product_id, item_data in self.cart.items():
                product = Product.objects.get(id=product_id)
                CartItemModel.objects.create(
                    cart=db_cart,
                    product=product,
                    quantity=item_data['quantity']
                )

    def add(self, product_id, price, title, quantity=1):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'price': str(price), 'title': title, 'quantity': quantity}
        self.session.modified = True
        self.save_to_db()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
            self.save_to_db()

    def clear(self):
        self.session['cart'] = {}
        self.cart = self.session['cart']
        self.session.modified = True
        self.save_to_db()

    def __iter__(self):
        for pid, item in self.cart.items():
            _item = item.copy()
            _item['id'] = int(pid)
            _item['price'] = Decimal(item['price'])
            _item['subtotal'] = _item['price'] * _item['quantity']
            yield _item

    def total(self):
        return sum(item['price'] * item['quantity'] for item in self.__iter__())
