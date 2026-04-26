## 01_baseline

### Configuración:

En esta primera corrida utilizamos la configuración base que definimos para comenzar a resolver el problema con PPO. Se trabajó con **CarRacing-v3** en su espacio de acción continuo original, manteniendo las tres componentes de acción (steering, gas y brake) sin modificaciones. Como observación usamos una imagen en grayscale con frame stacking de 4 frames, sin resize y sin cambios en la recompensa original del entorno. En cuanto al entrenamiento, se utilizó PPO con CnnPolicy:
- learning_rate = 1e-4
- n_envs = 8
- n_steps = 512
- batch_size = 128
- n_epochs = 10
- gamma = 0.99
- gae_lambda = 0.95
- clip_range = 0.2
- ent_coef = 0.0
- vf_coef = 0.5
- max_grad_norm = 0.5
- use_sde = True.

Esta configuración se eligió porque representaba un baseline razonable y estándar: por un lado, respetaba la naturaleza continua del problema y, por otro, permitía validar rápidamente el pipeline completo con una implementación robusta de PPO antes de comenzar a introducir ajustes más finos.

## Resultados:

Los resultados mostraron que el agente sí logró aprender algo útil, pero de forma claramente inestable.

En términos cuantitativos, el mejor resultado apareció temprano, en 50k timesteps, con un reward_mean de aproximadamente 380, mientras que la corrida terminó en 200k con un reward_mean cercano a 150, lo que indicó que la política no logró sostener su mejor desempeño. Además, varias evaluaciones mostraron una desviación estándar alta, señal de una política sensible al episodio particular.

En términos cualitativos, el video mostró que el auto tomaba correctamente la primera curva, pero luego comenzaba a oscilar en la segunda recta, se salía de la pista en la segunda curva y finalmente quedaba girando fuera de la pista.

En conjunto, estos resultados indicaron que la configuración de base era suficiente para producir aprendizaje, pero no para obtener una política estable y robusta: había una conducta local razonable al inicio, pero no una estrategia de conducción sostenida.

Se puede ver el detalle de los resultados en la notebook eval y en el video.
