from abstra.forms import *
from abstra.workflows import get_data, set_data

display_markdown("""
<img src="https://abstracloud-webflow-assets.s3.amazonaws.com/7626icon.png" width="50" height="50" />

# CreditOps
### Revisão de pedido de empréstimo
                 """, button_text="Começar")


user = get_user()

# if not user.email.endswith("abstra.app"):
#     display("Você não possui permissão para acessar este pedido.")
#     exit()

set_data("usuario_revisor", user.email)

nome = get_data("nome")
email = get_data("email")
renda = get_data("renda")
empregador = get_data("empregador")
valor_emprestimo = get_data("valor_emprestimo")
parcelas = get_data("parcelas")
score = get_data("score")
motivo_score_baixo = get_data("motivo_score_baixo")

markdown_text = f"""
# Pedido de Empréstimo

----------------------------

## Dados pessoais

### Nome: 
{nome}
### Email: 
{email}

----------------------------

## Dados de renda

### Renda: 
R$ {renda:,.2f}
### Empregador: 
{empregador}

----------------------------

## Dados de empréstimo

### Valor do empréstimo: 
R$ {valor_emprestimo:,.2f}
### Parcelas: 
{parcelas}

----------------------------

## Resultado Motor de Crédito

### Score: 
{score}
### Motivo: 
{motivo_score_baixo}

----------------------------
"""

selecao = Page() \
    .display_markdown(markdown_text) \
    .read_multiple_choice("Você deseja aprovar este pedido?",["Sim", "Não"]) \
    .run()

if selecao['Você deseja aprovar este pedido?'] == "Não":
    motivo_reprovacao = read_textarea("Motivo da reprovação")
    text = "reprovado"
    set_data("resultado", "reprovado")
    set_data("motivo_reprovacao", motivo_reprovacao)
else:
    set_data("resultado", "aprovado")
    text = "aprovado"

display_markdown(f"""
# Pedido {text}

Revisão feita por {user.email}
                 """, end_program=True, button_text=None)