"""Gera relatório Excel de pendências a partir de dados fictícios."""

from pathlib import Path

import pandas as pd


def gerar_relatorio(destino: Path | None = None):
    funcionarios = {
        "Nome": ["André Coutinho", "João Silva", "Maria Souza"],
        "CPF": ["111.111.111-11", "222.222.222-22", "333.333.333-33"],
        "Status": ["Regular", "Pendente", "Regular"],
    }
    dados = pd.DataFrame(funcionarios)
    pendencias = dados[dados["Status"] == "Pendente"].copy()

    if destino is None:
        destino = Path(__file__).resolve().parent / "relatorio_pendencias.xlsx"
    pendencias.to_excel(destino, index=False)
    return pendencias, destino


def main():
    try:
        pendencias, destino = gerar_relatorio()
    except (OSError, ImportError) as erro:
        print(f"Não foi possível gerar o relatório: {erro}")
        return 1
    print(f"Relatório de pendências criado: {destino}")
    print(pendencias)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
