from django.shortcuts import render
from core.models import risk
from core.forms import riskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class MainView(LoginRequiredMixin, View):
    login_url = 'account/login'
    def get(self, request):
        rc = risk.objects.all().count()
        all_risk = risk.objects.all()

        ctx = {'risk_count': rc, 'risk_list': all_risk}
        return render(request, 'core/index.html', ctx)

class riskCreate(LoginRequiredMixin, View):
    template = 'core/add.html'
    success_url = reverse_lazy('core:index')

    def get(self, request):
        form = riskForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = riskForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        risk = form.save()
        return redirect(self.success_url)


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class riskUpdate(LoginRequiredMixin, View):
    model = risk
    success_url = reverse_lazy('core:index')
    template = 'core/add.html'

    def get(self, request, pk):
        risk = get_object_or_404(self.model, pk=pk)
        form = riskForm(instance=risk)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        risk = get_object_or_404(self.model, pk=pk)
        form = riskForm(request.POST, instance=risk)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class riskDelete(LoginRequiredMixin, View):
    model = risk
    success_url = reverse_lazy('core:index')
    template = 'core/delete.html'

    def get(self, request, pk):
        risk = get_object_or_404(self.model, pk=pk)
        form = riskForm(instance=risk)
        ctx = {'risk': risk}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        risk = get_object_or_404(self.model, pk=pk)
        risk.delete()
        return redirect(self.success_url)
