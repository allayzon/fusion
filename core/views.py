from django.views.generic import FormView  # FormView só pq temos um form nosso, sen seria TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Equipe, Adicionais
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):  # Tem algo no contexto da página?
        context = super(IndexView, self).get_context_data(**kwargs)  # S? Então recupera
        context['servicos'] = Servico.objects.order_by('?').all()  # order_by('?') é para puxar aleatoriamente os obj
        context['equipe'] = Equipe.objects.order_by('?').all()  # Adicionando elementos ao context
        context['adicionais'] = Adicionais.objects.order_by('?').all()
        return context  # Passamos o contexto pra página index

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()  # Método que temos no final do formulário
        messages.success(self.request, 'E-mail enviado com sucesso.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail.')  # Mensagem de erro
        return super(IndexView, self).form_invalid(form, *args, **kwargs)  # Retorno do formulário