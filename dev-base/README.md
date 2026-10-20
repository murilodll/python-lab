# Sistema de vendas

Aplicação Streamlit para consultar vendas, cadastrar novos registros e acompanhar métricas em um dashboard. A interface também inclui uma aba para acompanhar a execução de testes manuais.

## Arquivos

- `main.py`: interface de vendas, dashboard e acompanhamento de testes.
- `vendas.csv`: dados carregados e atualizados pelo cadastro de vendas.
- `requirements.txt`: dependências Python do aplicativo.

## Requisitos

- Python 3
- Dependências listadas em `requirements.txt`

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Como executar

No terminal, dentro desta pasta:

```bash
streamlit run main.py
```

Use o formulário na barra lateral para cadastrar vendas. Os registros são salvos em `vendas.csv`. O dashboard apresenta o faturamento total e gráficos por vendedor e produto.

## Aba de testes manuais

A aba **Teste** carrega e atualiza um arquivo `testes.csv` no diretório de execução. Esse arquivo não está listado nesta pasta; ele existe em `testes-base`. Para usar a aba, disponibilize `testes.csv` em `dev-base` antes de iniciar o aplicativo. A aba permite filtrar os casos, alterar seus status e limpar a execução.
