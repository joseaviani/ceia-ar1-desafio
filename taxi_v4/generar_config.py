import gymnasium as gym
from PIL import Image


def guardar_captura_taxi(seed, filename):
  # Usamos rgb_array para capturar los píxeles
  env = gym.make("Taxi-v4", render_mode="rgb_array")
  env.reset(seed=seed)

  # Renderizamos y guardamos la imagen
  frame = env.render()
  img = Image.fromarray(frame)
  img.save(filename)
  env.close()


print("Generando capturas de configuraciones...")
guardar_captura_taxi(42, "taxi_conf1.png")
guardar_captura_taxi(123, "taxi_conf2.png")
guardar_captura_taxi(4, "taxi_conf3.png")
print("Imágenes generadas correctamente.")
