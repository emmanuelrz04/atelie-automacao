import pandas as pd
import os

# ===== 1. LER O EXCEL =====
print("📂 Lendo o Excel...")

# Pega o caminho absoluto do arquivo
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(pasta_atual, '..', 'dados', 'pedidos.xlsx')
caminho = os.path.normpath(caminho)

print(f"📁 Caminho: {caminho}")

if not os.path.exists(caminho):
    print("❌ Arquivo não encontrado!")
    print(f"   Verifique se o arquivo está em: {caminho}")
    exit(1)

df = pd.read_excel(caminho)
print(f" {len(df)} pedidos lidos")

# ===== 2. LIMPAR OS DADOS =====
print("\n🧹 Limpando os dados...")
df = df.dropna()
df['Data'] = pd.to_datetime(df['Data'])
print(f" {len(df)} pedidos válidos")

# ===== 3. CALCULAR O LUCRO =====
print("\n Calculando o lucro...")
df['Lucro'] = df['Valor'] - df['Custo']
lucro_total = df['Lucro'].sum()
print(f" Lucro total: R$ {lucro_total:.2f}")

# ===== 4. AGRUPAR POR CLIENTE =====
print("\n Agrupando por cliente...")
por_cliente = df.groupby('Cliente').agg({
    'Valor': 'sum',
    'Custo': 'sum',
    'Lucro': 'sum'
}).reset_index()
print(por_cliente)

# ===== 5. AGRUPAR POR STATUS =====
print("\n📊 Agrupando por status...")
por_status = df.groupby('Status').agg({
    'Valor': 'sum',
    'Lucro': 'sum'
}).reset_index()
print(por_status)

# ===== 6. AGRUPAR POR MÊS =====
print("\n📅 Agrupando por mês...")
df['Mes'] = df['Data'].dt.strftime('%m/%Y')
por_mes = df.groupby('Mes').agg({
    'Valor': 'sum',
    'Custo': 'sum',
    'Lucro': 'sum'
}).reset_index()
print(por_mes)

# ===== 7. GERAR O EXCEL DE SAÍDA =====
print("\n📝 Gerando relatório...")
caminho_saida = os.path.join(pasta_atual, '..', 'dados', 'relatorio.xlsx')
caminho_saida = os.path.normpath(caminho_saida)

with pd.ExcelWriter(caminho_saida) as writer:
    df.to_excel(writer, sheet_name='Pedidos', index=False)
    por_cliente.to_excel(writer, sheet_name='Por Cliente', index=False)
    por_status.to_excel(writer, sheet_name='Por Status', index=False)
    por_mes.to_excel(writer, sheet_name='Por Mês', index=False)

print(f"✅ Relatório gerado: {caminho_saida}")