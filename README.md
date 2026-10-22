# Relatório de Pendências com Python e Pandas

Projeto de estudo que cria uma tabela de colaboradores **fictícios**, filtra os registros com status **Pendente** e exporta o resultado para uma planilha Excel.

## Objetivo

Praticar manipulação de tabelas e exportação de relatórios automatizados com Python.

## Funcionamento

1. O script `Script.py` cria um `DataFrame` a partir de dados de demonstração.
2. Seleciona as linhas cujo campo `Status` é `Pendente`.
3. Grava o resultado em `relatorio_pendencias.xlsx`.
4. Exibe o resultado no terminal.

O arquivo Excel gerado também foi incluído no repositório como exemplo de saída.

## Tecnologias

- Python 3
- Pandas para tratamento dos dados
- OpenPyXL como mecanismo de exportação para `.xlsx`

## Arquivos

```text
Relatorio_de_Pendencias/
├── Script.py                    # gera o relatório
├── relatorio_pendencias.xlsx    # exemplo de saída
└── README.md
```

## Como executar

```powershell
git clone https://github.com/Coutin061017/Relatorio_de_Pendencias.git
cd Relatorio_de_Pendencias
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python Script.py
```

O script gera ou sobrescreve `relatorio_pendencias.xlsx` **no diretório a partir do qual for executado**.

## O que aprendi

- Criar e filtrar `DataFrames`.
- Aplicar filtros por status.
- Exportar resultados para Excel.
- Automatizar relatórios simples com Python.

> **Dados de exemplo:** os nomes e CPFs utilizados no script são demonstrativos; não representam uma fonte oficial e não devem ser usados como cadastro real.

**Autor:** [André Coutinho](https://github.com/Coutin061017)
