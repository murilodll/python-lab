# Titulo do Projeto: Sistema de Vendas
# Seção de Cadastro de Vendas
  # Campos Data, Vendedor, Produto, Quantidade, Valor Unitário, Cadastrar Venda
  # Botão Cadastrar Venda
    # Quando usuário clicar no botão Cadastrar Venda na tela de cadastro de vendas
    # Atualizar Dashboard com a nova venda cadastrada
# Seção Vendas Cadastradas
  # Mostrar Vendas Cadastradas em Tabela
# Seção Dashboard
  # Card/Metrica: Faturamento Total
  # Grafico de Barra: Vendas por Vendedor
  # Grafico de Pizza: Vendas por Produto

# Bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Dados
tabela_vendas = pd.read_csv("vendas.csv")
vendedores = ["Murilo", "Patricia", "Otto", "Nami"]
produtos = ["Notebook", "Monitor", "Memoria RAM", "Teclado", "Mouse"]

st.title("Sistema de Vendas")
tab_vendas, tab_dashboard, tab_teste = st.tabs(["Vendas Cadastradas", "Dashboard", "Teste"])


# ================ Tela de Cadastro de Vendas ================

st.sidebar.write("## Cadastro de Vendas")
data = st.sidebar.date_input("Data da Venda") # format="DD/MM/YYYY
vendedor = st.sidebar.selectbox("Vendedor", vendedores)
produto = st.sidebar.selectbox("Produto", produtos)
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor Unitário")
cadastrar_venda = st.sidebar.button("Cadastrar Venda")

# Botão Cadastrar Venda
if cadastrar_venda:
    if not data or not vendedor or not produto or not quantidade or not valor:
        st.sidebar.error("Por favor, preencha todos os campos antes de cadastrar a venda.")
    elif quantidade <= 0 or valor <= 0:
        st.sidebar.error("Quantidade e Valor Unitário devem ser maiores que zero.")
    else:
      nova_venda = [str(data), vendedor, produto, quantidade, valor]
      tabela_vendas.loc[len(tabela_vendas)] = nova_venda
      tabela_vendas.to_csv("vendas.csv", index=False)
      st.success(f"Venda cadastrada para {vendedor} com sucesso!")


# ================ Tela de Vendas Cadastradas ================

with tab_vendas:
  st.write("## Vendas Cadastradas")
  st.dataframe(tabela_vendas)


# ================ Tela de Dashboard ================

with tab_dashboard:
  st.write("## Dashboard de Vendas")

  faturamento_total = tabela_vendas["valor"].sum()
  st.metric("Faturamento Total", formatar_moeda(faturamento_total), "R$")

  grafico_vendas_por_vendedor = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto", title="Vendas por Vendedor")
  st.plotly_chart(grafico_vendas_por_vendedor)

  grafico_vendas_por_produto = px.pie(tabela_vendas, names="produto", values="valor", hole=0.1, title="Vendas por Produto")
  st.plotly_chart(grafico_vendas_por_produto)

with tab_teste:

  NOME_ARQUIVO_CSV = "testes.csv"

  # 1. INICIALIZAÇÃO DO SESSION STATE
  if "df_testes" not in st.session_state:
      df = pd.read_csv(NOME_ARQUIVO_CSV)
      df.columns = df.columns.str.strip()
      st.session_state.df_testes = df

  # 2. MAPEAMENTO DE STATUS
  STATUS_MAP = {
      0: ("0 - Não executado", "⚪"),
      1: ("1 - Sucesso", "🟢"),
      2: ("2 - Falha", "🔴"),
      3: ("3 - Bloqueado", "🟡")
  }

  COLOR_MAP = {
    "0 - Não executado": "#95A5A6",  # Cinza
    "1 - Sucesso": "#2ECC71",        # Verde
    "2 - Falha": "#E74C3C",          # Vermelho
    "3 - Bloqueado": "#F1C40F"       # Amarelo
  }

  OPCOES_RADIO = [val[0] for val in STATUS_MAP.values()]
  TEXTO_PARA_INT = {val[0]: key for key, val in STATUS_MAP.items()}

  st.title("Execução de Testes Manuais")

  # 3. FILTROS NA INTERFACE
  col1, col2 = st.columns(2)

  with col1:
      funcionalidades = ["Todas"] + list(st.session_state.df_testes["funcionalidade"].unique())
      filtro_func = st.selectbox("Filtrar por Suíte:", funcionalidades)

  with col2:
      status_opcoes = ["Todos"] + OPCOES_RADIO
      filtro_status = st.selectbox("Filtrar por Status:", status_opcoes)

  # 4. APLICAR FILTROS AO DATAFRAME
  df_exibicao = st.session_state.df_testes.copy()

  if filtro_func != "Todas":
      df_exibicao = df_exibicao[df_exibicao["funcionalidade"] == filtro_func]

  if filtro_status != "Todos":
      status_num = TEXTO_PARA_INT[filtro_status]
      df_exibicao = df_exibicao[df_exibicao["estado"] == status_num]

  st.divider()

  # 5. RENDERIZAR EXPANDERS DOS TESTES
  for index, row in df_exibicao.iterrows():
      test_id = row['id']
      suite = str(row['funcionalidade']).strip()
      nome = str(row['nome']).strip()
      descricao = str(row['descricao']).strip()
      estado_atual_num = int(row['estado'])

      status_texto, icone = STATUS_MAP.get(estado_atual_num, STATUS_MAP[0])
      titulo_expander = f"{icone} [{suite}] ID {test_id}: {nome} — ({status_texto})"

      with st.expander(titulo_expander):
          st.markdown("**Cenário:**")
          st.code(descricao, language="gherkin")
          
          novo_status_texto = st.radio(
              label="Alterar Status:",
              options=OPCOES_RADIO,
              index=OPCOES_RADIO.index(status_texto),
              key=f"radio_teste_{test_id}"
          )

          novo_status_num = TEXTO_PARA_INT[novo_status_texto]
          
          # Salva a alteração no DataFrame e reescreve o arquivo CSV em disco
          if novo_status_num != estado_atual_num:
              idx_original = st.session_state.df_testes[st.session_state.df_testes['id'] == test_id].index[0]
              st.session_state.df_testes.at[idx_original, 'estado'] = novo_status_num
              st.session_state.df_testes.to_csv(NOME_ARQUIVO_CSV, index=False)
              st.rerun()

  st.divider()

  if st.button("🔄 Limpar Execução", type="secondary", use_container_width=True):
      # 1. Reseta a coluna de estado para 0 no DataFrame e salva no arquivo CSV
      st.session_state.df_testes['estado'] = 0
      st.session_state.df_testes.to_csv(NOME_ARQUIVO_CSV, index=False)
      
      # 2. Remove as chaves salvas dos radios no session_state para redefinir os botões na tela
      for test_id in st.session_state.df_testes['id']:
          key_radio = f"radio_teste_{test_id}"
          if key_radio in st.session_state:
              del st.session_state[key_radio]
              
      st.rerun()

  # 5. DASHBOARD PLOTLY (GRÁFICO PIE / DONUT)
  st.subheader("📊 Progresso das Execuções")

  # Contagem dos status para o gráfico
  df_counts = (
      df_exibicao['estado']
      .map(lambda x: STATUS_MAP.get(int(x), STATUS_MAP[0])[0])
      .value_counts()
      .reset_index()
  )
  df_counts.columns = ['Status', 'Quantidade']

  fig = px.pie(
      df_counts,
      names='Status',
      values='Quantidade',
      color='Status',
      color_discrete_map=COLOR_MAP,
      hole=0.4  # Estilo Donut
  )

  fig.update_traces(textposition='inside', textinfo='percent+value')
  fig.update_layout(margin=dict(t=20, b=20, l=10, r=10), showlegend=True)

  st.plotly_chart(fig, use_container_width=True)