# Postmortem Resume Script

Este repositório contém um script Python para automatizar a extração de problemas e soluções detalhadas de documentos de post-mortem, gerando arquivos em Markdown prontos para uso em uma base de dados de FAQ.

## Propósito

- Extrair automaticamente, de documentos de post-mortem apenas o problema e a solução adotada, de forma detalhada.
- Gerar arquivos Markdown padronizados para facilitar a consulta e construção de uma base de conhecimento/FAQ com IA.

## Instalação

1. Clone este repositório:

```bash
git clone <url-do-repo>
cd postmortem
```

2. Crie e ative um ambiente virtual (venv):

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` com a variável de ambiente "GOOGLE_API_KEY" (necessária para o uso do Gemini).

## Como usar

1. Coloque os arquivos de post-mortem originais (Word, PDF, etc.) na pasta `postmortem-original-docs`.
2. Execute o script principal:

```bash
python resume.py
```

3. Os arquivos resumidos em Markdown serão gerados na pasta `docs/postmortems`.

---

**Observação:**
- Certifique-se de configurar corretamente as credenciais da API do LLM no arquivo `.env`.
- O script utiliza a biblioteca [docling](https://github.com/docling/docling) para conversão de documentos e [langchain-google-genai](https://python.langchain.com/docs/integrations/chat/google_genai/) para interação com o modelo de linguagem.
