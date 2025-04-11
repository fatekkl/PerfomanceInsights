## 📘 Documentação Completa do Projeto: **Performance Insights**

### 🎯 Objetivo
Criar um painel interativo que analisa campanhas de marketing digital (Google Ads e Facebook Ads), gerando métricas importantes como CTR, CPC, conversões, custo por conversão, etc. A ideia é centralizar os dados, tratá-los com Python, armazená-los no modelo BigQuery e visualizá-los no Looker Studio.

---

### 🧾 Estrutura dos Dados

O arquivo **`campanhas.csv`** possui os seguintes campos:

| Campo         | Tipo    | Descrição                                     |
| ------------- | ------- | --------------------------------------------- |
| `date`        | Data    | Data da execução da campanha                  |
| `name`    | Texto   | Nome da campanha                              |
| `platform`    | Texto   | Plataforma (Google ou Facebook)               |
| `impressions` | Inteiro | Quantidade de vezes que o anúncio foi exibido |
| `clicks`      | Inteiro | Quantidade de cliques no anúncio              |
| `conversions` | Inteiro | Quantidade de conversões (ex: compras)        |
| `cost`        | Decimal | Valor gasto com a campanha no dia             |

---

### ⚙️ Processamento com Python

O projeto é responsável por:
1. **Carregar os dados**
2. **Calcular as métricas derivadas**:
   - CTR (%)
   - CPC (Custo por Clique)
   - Taxa de Conversão (%)
   - Custo por Conversão

```python
CTR = clicks / impressoes * 100
CPC= custo / clicks
Taxa de Conversão (%) = conversoes / cliques * 100
Custo por Conversão (R$) = custo / conversoes
```

---

### ☁️ BigQuery

- Você vai usar o Python para enviar os dados tratados para o BigQuery.
- A tabela pode se chamar `campanhas_tratadas` dentro de um dataset como `marketing_insights`.

---

### 📊 Visualização no Looker Studio

Crie um dashboard com:
- Gráfico de linha (CPC e CTR ao longo do tempo)
- Gráfico de barras (conversões por campanha)
- Filtros por data e plataforma
- Tabela com métricas detalhadas

---

### 🧠 Extensões futuras (ideias para evoluir depois):
- Conectar diretamente às APIs do Google Ads / Facebook Ads.
- Adicionar análise de tendência com regressão linear.
- Incluir análise de sentimento de comentários (usando NLP).
- Automatizar envio diário com Google Cloud Scheduler + Cloud Functions.

---