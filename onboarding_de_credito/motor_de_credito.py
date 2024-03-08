from abstra.workflows import get_data, set_data
from time import sleep

nome = get_data("nome")
email = get_data("email")
renda = get_data("renda")
empregador = get_data("empregador")
valor_emprestimo = get_data("valor_emprestimo")
parcelas = get_data("parcelas")

if valor_emprestimo > renda * 0.3:
    set_data("score", "baixo")
    set_data("motivo_score_baixo", "Valor do empréstimo maior que 1/3 da renda")
else:
    set_data("score", "alto")

sleep(10)