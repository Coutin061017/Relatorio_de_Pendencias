import pandas as pd


funcionarios = {
    "Nome": [
        "André Coutinho",
        "João Silva",
        "Maria Souza"
    ],
    "CPF": [
        "111.111.111-11",
        "222.222.222-22",
        "333.333.333-33"
    ],
    "Status": [
        "Regular",
        "Pendente",
        "Regular"
    ]
}

df = pd.DataFrame(funcionarios)


pendencias = df[df["Status"] == "Pendente"]


pendencias.to_excel("relatorio_pendencias.xlsx", index=False)

print("Relatório de pendências criado com sucesso!")
print(pendencias)