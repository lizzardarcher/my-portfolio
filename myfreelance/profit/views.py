# -*- encoding: utf-8 -*-
# from django.shortcuts import render
# import math
# from datetime import datetime
# import datetime as dt
# import os

from django.contrib.messages.views import SuccessMessageMixin
# from django.db.models import Q
# from django.http import HttpResponse
# from django.template import loader
# from django.urls import reverse, reverse_lazy
# from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (ListView, DeleteView, UpdateView, CreateView, TemplateView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render
# from django.forms import modelformset_factory
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.http import HttpResponseRedirect
from .models import *
from .forms import *

class IndexPage(TemplateView):
    template_name = 'home/index.html'

class PortfolioTemplateView(TemplateView):
    template_name = 'home/portfolio.html'

class ProjectListView(SuccessMessageMixin, LoginRequiredMixin, ListView):
    model = Project
    ordering = ['-status']
    template_name = 'home/projects.html'
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        projects = Project.objects.all()
        additional_payments = AdditionalPayments.objects.all()
        support_payments = SupportPayments.objects.all()
        total_income = 0
        for i in projects:
            total_income += i.income
        for i in support_payments:
            total_income += i.price
        for i in additional_payments:
            total_income += i.price
        context.update({
            'total_income': total_income,
            'additional_payments': additional_payments,
            'support_payments': support_payments,
        })
        return context

class ProjectDetailsView(SuccessMessageMixin, LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'home/project_details.html'
    context_object_name = 'project'

class ProjectCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'crud/create.html'
    form_class = ProjectForm
    success_url = '/projects'
    success_message = 'Проект успешно добавлен!'


class PortfolioProjectCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Portfolio
    template_name = 'crud/create.html'
    form_class = PortfolioProjectForm
    success_url = '/projects'
    success_message = 'Проект успешно добавлен!'

class ProjectUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'crud/create.html'
    form_class = ProjectForm
    success_message = f'Проект успешно обновлён!'
    success_url = '/projects'

class ProjectDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/projects'
    template_name = 'crud/delete.html'
    success_message = 'Проект успешно удален!'
    context_object_name = 'object'


class SupportPaymentsDetailsView(SuccessMessageMixin, LoginRequiredMixin, DetailView):
    model = SupportPayments
    template_name = 'home/support_payment_details.html'
    context_object_name = 'sp'

class SupportPaymentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = SupportPayments
    form_class = SupportPaymentsForm
    template_name = 'crud/create.html'
    context_object_name = 'support_payments'
    success_url = '/projects'
    success_message = 'Платёж успешно добавлен!'

class SupportPaymentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = SupportPayments
    template_name = 'crud/create.html'
    form_class = SupportPaymentsForm
    success_message = 'Платёж успешно обновлён!'

    def get_success_url(self):
        return f'/support_payment_details/{str(self.request.META.get("HTTP_REFERER")).split("/")[-1]}'

class SupportPaymentsDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = SupportPayments
    success_url = '/projects'
    template_name = 'crud/delete.html'
    success_message = 'Платёж успешно удален!'


class AdditionalPaymentsCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = AdditionalPayments
    form_class = AdditionalPaymentsForm
    template_name = 'crud/create.html'
    context_object_name = 'additional_payments'
    success_url = '/projects'
    success_message = 'Платёж успешно добавлен!'

class AdditionalPaymentsUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdditionalPayments
    form_class = AdditionalPaymentsForm
    template_name = 'crud/create.html'
    success_message = 'Платёж успешно обновлён!'

    def get_success_url(self):
        return f'/additional_payment_details/{str(self.request.META.get("HTTP_REFERER")).split("/")[-1]}'

class AdditionalPaymentsDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = AdditionalPayments
    success_url = '/projects'
    template_name = 'crud/delete.html'
    success_message = 'Платёж успешно удален!'
