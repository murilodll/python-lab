# Chatbot com IA

Aplicação de conversa criada com Streamlit. As mensagens são enviadas a um modelo Gemini pela API compatível com o formato da biblioteca OpenAI, e o histórico fica na sessão atual do Streamlit.

## Arquivos

- `main.py`: interface e integração com a API.
- `chave.py`: módulo de onde o aplicativo importa `API_KEY`.

## Requisitos

- Python 3
- streamlit
- openai
- Uma chave de API válida para o serviço configurado no aplicativo

Instale as dependências:

```bash
python -m pip install streamlit openai
```

## Configuração e execução

O código espera encontrar `API_KEY` no módulo `chave.py`. Configure uma chave válida antes de iniciar o aplicativo e execute, nesta pasta:

```bash
streamlit run main.py
```

Não publique nem compartilhe chaves de API. O arquivo `chave.py` contém uma credencial no estado atual do projeto; se ela for válida, revogue-a no provedor e gere outra. Para uso compartilhado ou publicação do projeto, prefira carregar o segredo por uma variável de ambiente ou pelo mecanismo de secrets do Streamlit, em vez de mantê-lo no código.
