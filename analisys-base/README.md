# Análise de cancelamentos

Notebook de análise exploratória de dados de clientes, com foco em identificar fatores associados ao cancelamento.

## Conteúdo

- `main.ipynb`: carrega e prepara os dados, calcula a distribuição de cancelamentos e exibe histogramas por variável.
- `cancelamentos.csv`: base de dados utilizada. Inclui informações como duração do contrato, ligações ao call center, dias de atraso e status de cancelamento.

O notebook também compara os cancelamentos antes e depois de filtrar contratos mensais, atrasos acima de 20 dias e mais de quatro ligações ao call center. As observações e conclusões estão registradas nas células do notebook.

## Requisitos

- Python 3
- Jupyter Notebook
- pandas
- plotly

Instale as dependências:

```bash
python -m pip install jupyter pandas plotly
```

## Como executar

No terminal, dentro desta pasta:

```bash
jupyter notebook main.ipynb
```

Execute as células em ordem. O notebook espera encontrar `cancelamentos.csv` nesta mesma pasta.
