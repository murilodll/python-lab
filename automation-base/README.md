# Automação de cadastro de produtos

Automação de interface gráfica que lê produtos de um CSV, abre o navegador Opera e preenche o formulário de cadastro do site de treinamento.

## Arquivos

- `main.py`: abre o site, realiza o login configurado no código e cadastra cada linha de `produtos.csv`.
- `posicao.py`: aguarda cinco segundos e imprime a posição atual do mouse, para ajudar a conferir as coordenadas usadas pela automação.
- `produtos.csv`: lista de produtos com código, marca, tipo, categoria, preço, custo e observação.

## Requisitos

- Python 3
- Navegador Opera instalado (Ou altere a variável no começo do arquivo)
- pandas
- pyautogui

Instale as dependências:

```bash
python -m pip install pandas pyautogui
```

## Como executar

Abra um terminal nesta pasta e execute:

```bash
python main.py
```

Antes de executar, confira no `main.py` o endereço do site, os dados de login e as coordenadas dos campos. As coordenadas dependem da resolução, da escala e do layout da tela. Mantenha o navegador e a sessão de desktop disponíveis enquanto a automação estiver rodando; ela controla teclado e mouse.

Para conferir a posição do mouse:

```bash
python posicao.py
```
