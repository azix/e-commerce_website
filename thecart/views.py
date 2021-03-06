from django.shortcuts import render_to_response
from django.template import RequestContext
from thecart import cart


def show_cart(request, template_name="thecart/cart.html"):
    cart_item_count = cart.cart_item_count(request)
    page_title = 'Shopping Cart'
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
