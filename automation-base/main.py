# Projeto de Estudo Para Python - Cadastro de Produtos
# Desenvolvido por: Murilo Lacerda
# Objetivo: Entrar em um sistema (website) realizar login e cadastrar produtos no sistema usando csv como lista de produtos.

# Bibliotecas
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5
NAVEGADOR = "opera"

# Abrindo o navegador
pyautogui.press("win")
pyautogui.write(NAVEGADOR)
pyautogui.press("enter")
time.sleep(2)

# Variáveis
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
login = "Email@login.com"
senha = "senha123"
posicaoCampoLogin = (914, 392)
posicaoCampoCodigo = (839, 277)
tabelaProdutos = pd.read_csv("produtos.csv")

# Entrar no site
pyautogui.write(site)
pyautogui.press("enter")
time.sleep(3)

# Fazer Login
pyautogui.click(posicaoCampoLogin)
pyautogui.write(login)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")
time.sleep(3)

# Preencher o formulário de cadastro de produtos
for coluna in tabelaProdutos.itertuples(index=False):
    pyautogui.click(posicaoCampoCodigo)
    pyautogui.write(str(coluna.codigo))
    pyautogui.press("tab")
    pyautogui.write(str(coluna.marca))
    pyautogui.press("tab")
    pyautogui.write(str(coluna.tipo))
    pyautogui.press("tab")
    pyautogui.write(str(coluna.categoria))
    pyautogui.press("tab")
    pyautogui.write(str(coluna.preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(coluna.custo))
    pyautogui.press("tab")
    obs = coluna.obs
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("enter")

    # Volta Pro Topo do Formulário
    pyautogui.scroll(5000)
