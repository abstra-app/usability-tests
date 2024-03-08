from abstra.forms import *
from abstra.workflows import set_data
import requests

display_markdown("""
<img src="https://abstracloud-webflow-assets.s3.amazonaws.com/5599illustration.gif" width="100" height="100" />

# Faça um empréstimo pessoal 🫰
### Simples, rápido e sem burocracia.

Preencha este formulário para solicitar um empréstimo pessoal e receba uma resposta rápida!
""", button_text="Começar")

dados_pessoais = Page() \
    .display("Informações pessoais", size="large") \
    .read("Nome completo", placeholder = "Michael Scott") \
    .read_email("Email", placeholder = "michael.scott@dundermifflin.com") \
    .run()

dados_renda = Page() \
    .display("Informações de renda", size="large") \
    .read_currency("Renda mensal?", currency = "BRL", placeholder = "10.000,00") \
    .read("Empregador atual, caso exista", placeholder = "Dunder Mifflin") \
    .run()

dados_emprestimo = Page() \
    .display("Informações de empréstimo", size="large") \
    .read_currency("Valor do empréstimo", currency="BRL", placeholder = "10.000,00") \
    .read("Quantidade de parcelas", placeholder = "12", min=2, max=12) \
    .run()


set_data("nome", dados_pessoais["Nome completo"])
set_data("email", dados_pessoais["Email"])
set_data("renda", dados_renda["Renda mensal?"])
set_data("empregador", dados_renda["Empregador atual, caso exista"])
set_data("valor_emprestimo", dados_emprestimo["Valor do empréstimo"])
set_data("parcelas", dados_emprestimo["Quantidade de parcelas"])

display_markdown("""
# ✨ Pedido recebido!
### Sua avaliação levará até 10 minutos. Você receberá um email com o resultado.
""", end_program=True, button_text=None)