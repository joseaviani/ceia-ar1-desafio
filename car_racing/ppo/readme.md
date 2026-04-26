## Car Racing con Gymnasium y PPO

En el folder `corridas` se encuentra un subfolder por cada experimento realizado, donde se documenta en detalle la configuración utilizada en cada corrida, la motivación detrás de ese cambio respecto de la corrida anterior y los resultados obtenidos tanto a nivel cuantitativo como cualitativo; además, en el folder `videos` de cada corrida pueden verse los episodios grabados para analizar visualmente el comportamiento del agente.

Particularmente interesantes son [`01_baseline`](corridas/01_baseline), donde se describe en detalle la configuración utilizada, y [`10_observation_resize`](corridas/10_observation_resize), donde se puede ver el detalle de la los mejores resultados.

### Mejor corrida:

La mejor corrida obtenida fue [`10_observation_resize`](corridas/10_observation_resize), ya que combinó un rendimiento cuantitativo alto con un comportamiento cualitativo claramente superior al de las corridas anteriores: alcanzó rewards elevados de forma sostenida, mostró una conducción más estable y logró completar correctamente una vuelta, mientras que en otras configuraciones observamos con mayor frecuencia oscilaciones, salidas de pista o recuperación en sentido incorrecto. Además, las corridas multiseed basadas en esta configuración mostraron que el cambio de observación mediante resize fue una mejora relevante y no solo un resultado aislado. En el video se puede ver que el agente completa una vuelta correctamente: [`video`](corridas/10_observation_resize/experiments/carracing_ppo/run_20260424_113851_seed0/videos/best_model_eval-step-0-to-step-2000.mp4)

Se puede ver el detalle de los resultados de esa corrida en la notebook eval y en el video.