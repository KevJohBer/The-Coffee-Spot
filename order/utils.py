"""
Order App - utils

utils for order app
"""

from threading import Timer
from .models import Order


def prep_time(order_id):
    """ Sets timer to when the coffee is ready """
    order = Order.objects.get(id=order_id)

    def done():
        order.active = False
        order.save()

    timer = Timer(900, done)
    timer.start()
