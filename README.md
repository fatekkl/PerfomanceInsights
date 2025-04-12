# 📘 Performance Insights — Documentação do Projeto

Um painel interativo para análise de campanhas de marketing digital com Python + Looker Studio.

🔗 [Veja o Painel no Looker Studio](https://lookerstudio.google.com/reporting/f81898e2-893b-426a-b2d3-68459afc02f0)

---

## 🎯 Objetivo

Criar um painel interativo que analisa campanhas de marketing digital (Google Ads e Facebook Ads), gerando métricas importantes como CTR, CPC, conversões, custo por conversão (CPA), etc.

Os dados são carregados a partir de arquivos CSV, tratados em Python com métricas de desempenho e exportados para um formato pronto para visualização no Looker Studio. Isso permite uma análise rápida e interativa sem depender diretamente das plataformas originais.

---

## 🧾 Estrutura dos Dados

### 📂 Arquivos de Dados

#### `campanhas.csv` (dados brutos)
Contém os dados exportados das plataformas de marketing.

| Campo         | Tipo CSV | Tipo BigQuery | Descrição                                     |
| ------------- | -------- | ------------- | --------------------------------------------- |
| `date`        | Data     | `DATE`        | Data da execução da campanha                  |
| `name`        | Texto    | `STRING`      | Nome da campanha                              |
| `platform`    | Texto    | `STRING`      | Plataforma (Google ou Facebook)               |
| `impressions` | Inteiro  | `INTEGER`     | Quantidade de vezes que o anúncio foi exibido |
| `clicks`      | Inteiro  | `INTEGER`     | Quantidade de cliques no anúncio              |
| `conversions` | Inteiro  | `INTEGER`     | Quantidade de conversões (ex: compras)        |
| `cost`        | Decimal  | `FLOAT`       | Valor gasto com a campanha no dia             |

---

#### `handled_campaigns.csv` (dados tratados)

Após o processamento em Python, é gerado este arquivo com métricas calculadas:

| Campo         | Tipo CSV | Tipo BigQuery | Descrição                                     |
| ------------- | -------- | ------------- | --------------------------------------------- |
| `ctr`         | Decimal  | `FLOAT`       | Taxa de cliques por campanha (%)              |
| `cpc`         | Decimal  | `FLOAT`       | Custo médio por clique                        |
| `cpa`         | Decimal  | `FLOAT`       | Custo médio por conversão                     |

---

## ⚙️ Processamento com Python

O projeto realiza as seguintes etapas:

1. **Leitura de dados do `campanhas.csv`**
2. **Cálculo de métricas derivadas**:

### 📐 Fórmulas utilizadas

- **CTR (Click Through Rate)** = `(clicks / impressions) * 100`
- **CPC (Cost Per Click)** = `cost / clicks`
- **CPA (Cost Per Action)** = `cost / conversions`

⚠️ Todas as métricas são **arredondadas para duas casas decimais**. Divisões por zero são tratadas para evitar erros.

---

## 📊 Visualização no Looker Studio

O dashboard inclui:

- 📈 Gráfico de linha: CPC e CTR ao longo do tempo
- 📊 Gráfico de barras: conversões por campanha
- 🗓️ Filtros por data e plataforma
- 📋 Tabela com métricas detalhadas (CTR, CPC, CPA)

---

## ▶️ Como Executar

1. Coloque seu arquivo `campanhas.csv` na raiz do projeto.
2. Execute o script de processamento:

```bash
python main.py
