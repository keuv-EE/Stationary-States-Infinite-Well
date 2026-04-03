import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
a = 1
x = np.linspace(0, a, 1000)  # Domínio de 0 a a com 1000 pontos

# Criar primeira figura com subplots (3x3 grid, mas usaremos 2x4 para 7 plots)
fig1 = plt.figure(figsize=(12, 8))

# Loop para n = 1 até 7
for n in range(1, 8):
    # Calcular a função psi_n(x)
    psi_n = np.sqrt(2/a) * np.sin(n * np.pi * x / a)
    
    # Criar subplot (3x3 grid)
    ax = fig1.add_subplot(3, 3, n)
    
    # Plotar a função
    ax.plot(x, psi_n, 'b-', linewidth=2)
    ax.plot(x, np.zeros_like(x), 'k--', linewidth=0.5)  # Linha zero
    
    # Configurar o gráfico
    ax.set_xlabel('x')
    ax.set_ylabel(f'$\\psi_{n}(x)$')
    ax.set_title(f'n = {n}')
    ax.grid(True)
    ax.set_xlim([0, a])
    
    # Ajustar limites y baseado no valor máximo
    y_max = np.max(np.abs(psi_n))
    ax.set_ylim([-y_max*1.1, y_max*1.1])

# Ajustar o layout
fig1.suptitle('Funções de Onda $\\psi_n(x) = \\sqrt{2/a} \\sin(n\\pi x/a)$ para a = 1', fontsize=14)
plt.tight_layout()
plt.subplots_adjust(top=0.92)

# Versão alternativa: Todos os gráficos na mesma figura
fig2 = plt.figure(figsize=(10, 6))

# Cores para distinguir os diferentes n
colors = plt.cm.tab10(np.linspace(0, 1, 7))

for n in range(1, 8):
    psi_n = np.sqrt(2/a) * np.sin(n * np.pi * x / a)
    plt.plot(x, psi_n, color=colors[n-1], linewidth=1.5, label=f'n = {n}')

plt.plot(x, np.zeros_like(x), 'k--', linewidth=0.5)  # Linha zero

plt.xlabel('x')
plt.ylabel('$\\psi_n(x)$')
plt.title('Funções de Onda para n = 1 até 7 (a = 1)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.xlim([0, a])
plt.tight_layout()

# Mostrar as figuras
plt.show()

# Opcional: Salvar as figuras
# fig1.savefig('funcoes_onda_subplots.png', dpi=300, bbox_inches='tight')
# fig2.savefig('funcoes_onda_sobrepostas.png', dpi=300, bbox_inches='tight')