from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import TemplateView, DetailView

from sanApp.models import Product, Review


class HomeView(TemplateView):
    template_name = 'sanApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'sanApp/detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product__pk=kwargs['object'].id).order_by('-created_at')
        return context


class ReviewCreateView(View):

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=self.request.POST['pk'])
        Review.objects.create(user=request.user, product=product, comment=request.POST['comment'])
        return redirect('detail', product.pk)


class UserLoginRender(TemplateView):
    template_name = 'sanApp/login.html'


class UserRegisterRender(TemplateView):
    template_name = 'sanApp/register.html'


class UserLoginView(View):

    def get(self, request, *args, **kwargs):
        user = authenticate(request, username=request.GET['login'], password=request.GET['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'sanApp/login.html', context={'error': 'Неверный логин или пароль'})


class UserRegisterView(View):
    def post(self, *args, **kwargs):
        return 1
