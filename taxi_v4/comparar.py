import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt


def entrenar_agente(estrategia, episodios=4000):
  env = gym.make("Taxi-v4")
  q_table = np.zeros((env.observation_space.n, env.action_space.n))
  recompensas = []

  # Hiperparámetros base
  alpha = 0.1
  gamma = 0.99

  # Parámetros para el decaimiento
  min_epsilon = 0.001
  decay_rate = 0.002

  for episodio in range(episodios):
    state, _ = env.reset()
    terminated, truncated = False, False
    total_reward = 0

    # Seleccionar el epsilon según la estrategia
    tipo, epsilon_inicial = estrategia
    if tipo == 'dinamico':
      epsilon = min_epsilon + (epsilon_inicial - min_epsilon) * np.exp(-decay_rate * episodio)
      if episodio % 500 == 0:
        print(f"  [dinamico/{epsilon_inicial}] ep={episodio:4d} | epsilon={epsilon:.4f}")
    elif tipo == 'fijo':
      epsilon = epsilon_inicial

    while not terminated and not truncated:
      # Estrategia Epsilon-Greedy
      if np.random.rand() < epsilon:
        action = env.action_space.sample()
      else:
        action = np.argmax(q_table[state])

      next_state, reward, terminated, truncated, _ = env.step(action)

      # Ecuación de Q-Learning con máscara para estados terminales
      old_value = q_table[state, action]
      next_max = np.max(q_table[next_state])
      new_value = old_value + alpha * (reward + gamma * next_max * (1 - int(terminated)) - old_value)
      q_table[state, action] = new_value

      state = next_state
      total_reward += reward

    recompensas.append(total_reward)

  env.close()
  return recompensas


ESTRATEGIAS = [
    ['fijo', 0.2],
    ['dinamico', 0.9],
]

COLORES = ['#1f77b4', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b']
EPISODIOS = 4000
WINDOW = 100

resultados = []
for estrategia in ESTRATEGIAS:
    tipo, epsilon_inicial = estrategia
    print(f"Entrenando [{tipo} / e={epsilon_inicial}]...")
    recompensas = entrenar_agente(tuple(estrategia), episodios=EPISODIOS)
    resultados.append(recompensas)

print("Procesando datos y generando gráfico...")

plt.figure(figsize=(12, 6))
for i, (estrategia, recompensas) in enumerate(zip(ESTRATEGIAS, resultados)):
    tipo, epsilon_inicial = estrategia
    label = f"{'Dinámico' if tipo == 'dinamico' else 'Fijo'} $\\epsilon$={epsilon_inicial}"
    smooth = np.convolve(recompensas, np.ones(WINDOW) / WINDOW, mode='valid')
    plt.plot(smooth, label=label, color=COLORES[i % len(COLORES)], linewidth=2)

plt.xlabel('Episodios', fontsize=12)
plt.ylabel(f'Recompensa Total (Media Móvil {WINDOW} eps)', fontsize=12)
plt.legend(loc='lower right')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig('comparativa_epsilon.png', dpi=300)
plt.show()