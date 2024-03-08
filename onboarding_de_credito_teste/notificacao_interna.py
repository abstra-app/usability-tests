from abstra.workflows import get_data
from dotenv import load_dotenv
import os
import requests

load_dotenv()
slack_token = os.environ.get("SLACK_BOT_TOKEN")

nome = get_data("nome")
email = get_data("email")
renda = get_data("renda")
empregador = get_data("empregador")
valor_emprestimo = get_data("valor_emprestimo")
parcelas = get_data("parcelas")
score = get_data("score")
resultado = get_data("resultado")
motivo_reprovacao = get_data("motivo_reprovacao")
usuario_revisor = get_data("usuario_revisor")

# res = requests.post(
#         'https://slack.com/api/chat.postMessage',
#     json={
#         'channel': 'credit-onboarding-example',
#         'text': f"""
# 💰🚫 Novo pedido de crédito reprovado. Informações:

# - *Nome*: {nome}, 
# - *Email*: {email}, 
# - *Renda declarada*: R${renda:,.2f}, 
# - *Empregador*: {empregador}, 
# - *Valor do empréstimo*: R${valor_emprestimo:,.2f}, 
# - *Nº de parcelas*: {parcelas}, 
# - *Score*: {score}, 
# - *Motivo da reprovação*: {motivo_reprovacao}
# - *Revisor*: {usuario_revisor}
# """},
#     headers={
#         'Authorization': 'Bearer ' + slack_token,
#         'Content-type': 'application/json; charset=utf-8'
#     })

# print(res)

texto = """
- *Nome*: {nome}, 
- *Email*: {email}, 
- *Renda declarada*: R${renda:,.2f}, 
- *Empregador*: {empregador}, 
- *Valor do empréstimo*: R${valor_emprestimo:,.2f}, 
- *Nº de parcelas*: {parcelas}, 
- *Score*: {score}, 
- *Motivo da reprovação*: {motivo_reprovacao}
- *Revisor*: {usuario_revisor}"""

print(texto)