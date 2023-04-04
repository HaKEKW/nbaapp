from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from nba_shop.filters import GoodFilter
from nba_shop.forms import GoodForm, OrderForm
from nba_shop.models import Good, Order, Customer
from nba_shop.mixins import ObjectDetailMixin, ObjectUpdateMixin, ObjectDeleteMixin, ObjectCreateMixin


# Create your views here.
def view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        goods = Good.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
        myFilter = GoodFilter(request.GET, queryset=goods)
    else:
        goods = Good.objects.all()
        myFilter = GoodFilter(request.GET, queryset=goods)
        goods = myFilter.qs
    context = {'goods': goods, 'myFilter': myFilter}
    return render(request, 'nba_shop/index.html', context)


class GoodDetailView(ObjectDetailMixin, View):
    model = Good
    template = 'nba_shop/good_detail.html'


class AdminPanelView(View):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        customers = Customer.objects.all()
        total_customers = customers.count()
        total_orders = orders.count()
        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()
        template = 'nba_shop/admin_panel.html'
        context = {'orders': orders,
                   'customers': customers,
                   'total_customers': total_customers,
                   'total_orders': total_orders,
                   'delivered': delivered,
                   'pending': pending,
                   }

        return render(request, template, context)


class GoodView(ListView):
    model = Good
    template_name = 'nba_shop/products.html'
    context_object_name = 'goods'


class GoodUpdateView(ObjectUpdateMixin, View):
    model = Good
    form_model = GoodForm
    template = 'nba_shop/good_update.html'


class GoodDeleteView(ObjectDeleteMixin, View):
    model = Good
    template = 'nba_shop/good_delete.html'
    redirect_url = 'goods_url'


class GoodCreateView(ObjectCreateMixin, View):
    form_model = GoodForm
    template = 'nba_shop/good_create.html'


class OrderUpdateView(ObjectUpdateMixin, View):
    model = Order
    form_model = OrderForm
    template = 'nba_shop/order_update.html'

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        bound_form = self.form_model(request.POST, instance=obj)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('admin_panel_url')
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class OrderDeleteView(ObjectDeleteMixin, View):
    model = Order
    template = 'nba_shop/order_delete.html'
    redirect_url = 'admin_panel_url'


class CustomerPanelView(ObjectDetailMixin, View):
    model = Customer
    template = 'nba_shop/customer_info.html'

    def get(self, request, pk):
        customer = self.model.objects.get(pk=pk)
        orders = customer.order_set.all()
        order_count = orders.count()
        context = {'customer': customer, 'orders': orders, 'order_count': order_count}  # add filter later

        return render(request, self.template, context)
