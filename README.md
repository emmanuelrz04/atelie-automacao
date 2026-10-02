# Sistema de Automação Financeira - Ateliê de Costura

**Status do Projeto:** Em Produção | **Última Atualização:** Outubro/2026

---

## O Problema

Um ateliê de costura especializado em roupas de Carnaval, São João e 7 de Setembro controlava todos os pedidos e finanças em caderno e WhatsApp. O lucro real nunca era calculado corretamente, os prazos de entrega eram frequentemente estourados e não havia visibilidade sobre quais clientes ou produtos geravam mais retorno.

Tempo total perdido por mês: aproximadamente 8 horas apenas com tarefas manuais de organização e cálculo.

## A Solução

Script de automação que lê a planilha de pedidos do ateliê, limpa os dados, calcula o lucro real e gera relatórios profissionais automaticamente.

**Tecnologias utilizadas:**
- Python 3.14
- Pandas 2.2
- OpenPyXL 3.1
- Excel (.xlsx)

---

## Principais Funcionalidades

### Para o Ateliê

- Leitura automática da planilha de pedidos
- Limpeza e padronização dos dados
- Cálculo automático do lucro por pedido
- Agrupamento por cliente, status e mês
- Geração de relatório formatado em Excel

### Relatórios e Estatísticas

- Lucro total do período
- Lucro por cliente (quem dá mais retorno)
- Lucro por status (Aguardando, Produção, Entregue)
- Lucro por mês (evolução do negócio)
- Arquivo Excel com 4 abas prontas para análise

### Diferenciais

- Zero dependência de internet (funciona localmente)
- Processamento em segundos (antes levava horas)
- Relatórios prontos para o contador
- Fácil de adaptar para outros negócios

---

## Arquitetura

O projeto segue o padrão de script de automação com separação clara de responsabilidades:

`Leitura:` Leitura do arquivo Excel de entrada
`Limpeza:` Tratamento e padronização dos dados com Pandas
`Cálculo:` Geração dos indicadores financeiros
`Saída:` Exportação para Excel com múltiplas abas

### Diagrama de Fluxo de Dados

Excel de entrada → Pandas processa → Cálculos aplicados → Novo Excel gerado

---

## Benefícios Entregues

| Métrica | Antes | Depois |
|---------|-------|--------|
| Tempo de fechamento | 8 horas | 5 minutos |
| Precisão do lucro | Baixa | 100% |
| Relatórios por mês | Nenhum | 4 abas |
| Visão por cliente | Nenhuma | Automática |

**Diferenciais competitivos:**

-  Zero dependência de internet (funciona localmente)
-  Processamento em segundos
-  Fácil de adaptar para outros ateliês
-  Relatórios prontos para impressão

---

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior instalado
- Git (opcional, para clonar)

### Passos para rodar localmente

`git clone https://github.com/emmanuelrz04/atelie-automacao.git`

`cd atelie-automacao`

`python -m venv venv`

`venv\Scripts\activate` no Windows ou `source venv/bin/activate` no Linux/Mac

`pip install -r requirements.txt`

`cd codigo`

`python analise.py`

