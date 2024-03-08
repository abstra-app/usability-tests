from abstra.workflows import *
import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import *
from dotenv import load_dotenv

load_dotenv()
sendgrid_token = os.environ.get("SENDGRID_API_KEY")
sender_email = os.environ.get('SENDER_EMAIL')

nome = get_data("nome")
pnome = nome.split(" ")[0]
email = get_data("email")
renda = get_data("renda")
empregador = get_data("empregador")
valor_emprestimo = get_data("valor_emprestimo")
parcelas = get_data("parcelas")
score = get_data("score")
resultado = get_data("resultado")

html = f"""
<html>
<head>
    <style>
        .header-text {{
            font-size: 20px;
            font-weight: bold;
            color: #333;
            text-align: left;
        }}

        .paragraph-text {{
            font-size: 12px;
            color: #555;
            text-align: left;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div style="text-align: left; margin: 20px 0;">
        <img src="https://abstracloud-webflow-assets.s3.amazonaws.com/3750logo.png" width=200px>
    </div>
    <div class="header-text">
    {pnome}, boas notícias 🤑
    </div>
    <div class="paragraph-text">
        Seu empréstimo de R$ {valor_emprestimo:,.2f} foi aprovado! Dinheiro na mão é vendaval 💸💸 
        
        Em breve entraremos em contato para finalizar a contratação.
    </div>
</body>
</html>
"""

# message = Mail(
#         from_email=From(sender_email, "Scranton Credit [Abstra Example]"),
#         to_emails=email, 
#         subject=f"Empréstimo aprovado, {pnome}",
#         html_content=html)

# sg = SendGridAPIClient(sendgrid_token)
# response = sg.send(message)

# print(response.status_code)

texto = """
{pnome}, boas notícias 🤑

Seu empréstimo de R$ {valor_emprestimo:,.2f} foi aprovado! Dinheiro na mão é vendaval 💸💸 

Em breve entraremos em contato para finalizar a contratação."""

print(texto)