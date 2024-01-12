# admin_custom/views.py

from django.db.models import Count
from django.shortcuts import render
from chartjs.views.pie import HighChartDonutView
from produit.models import Produit
from category.models import Category

class ProductPercentageChart(HighChartDonutView):
    def get_labels(self):
        categories = Category.objects.annotate(product_count=Count('cproducts'))
        return [category.name for category in categories]

    def get_data(self):
        total_products = Produit.objects.count()
        categories = Category.objects.annotate(product_count=Count('cproducts'))
        data = [category.product_count / total_products * 100 for category in categories]
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labels'] = self.get_labels()
        context['data'] = self.get_data()
        return context

    def render_to_response(self, context, **response_kwargs):
        return render(self.request, 'admin_custom/product_percentage_chart.html', context)

product_percentage_chart = ProductPercentageChart.as_view()
