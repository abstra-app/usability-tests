from abstra.workflows import get_data, set_data
from time import sleep

nome = get_data("nome")
email = get_data("email")
renda = get_data("renda")
empregador = get_data("empregador")
valor_emprestimo = get_data("valor_emprestimo")
parcelas = get_data("parcelas")
score = get_data("score")

if valor_emprestimo < 100000000:
    set_data("resultado", "aprovado")
else: 
    set_data("resultado", "reprovado")
    set_data("motivo_reprovacao", "Valor do empréstimo muito alto")

sleep(10)