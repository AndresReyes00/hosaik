from django.views.generic import TemplateView

# Create your views here.


class MoraView(TemplateView):
    template_name = "./mora/mora.html"
