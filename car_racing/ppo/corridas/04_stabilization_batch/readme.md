## 04_stabilization_batch

### Configuración:

Dado que `03_stabilization_sde_off` fue la mejor corrida hasta ese momento, para esta nueva prueba tomamos esa configuración como base y aplicamos un único cambio: aumentar el `batch_size` de **128** a **256**. El motivo fue que, si bien en la corrida anterior el agente había mejorado claramente en reward, seguía mostrando bastante variabilidad entre episodios y un comportamiento visual frágil. Aumentar el tamaño de batch era una forma simple de intentar suavizar las actualizaciones de PPO y reducir el ruido del entrenamiento.

## Resultados:

Los resultados cuantitativos mostraron que esta corrida sí logró aprender, pero de forma más lenta y sin superar a `03_stabilization_sde_off`. Durante la primera mitad del entrenamiento el `reward_mean` se mantuvo en valores negativos o muy bajos, recién mostrando una mejora clara a partir de 125k timesteps. A partir de allí alcanzó aproximadamente **134.1** en 125k, **173.9** en 150k y un pico de **375.8** en 175k, para finalizar en **188.4** a 200k. Aunque estos valores fueron mejores que los de `02_stabilization_lr`, quedaron por debajo de los de `03_stabilization_sde_off`, tanto en el mejor punto como en el resultado final.

En términos cualitativos, el video mostró un comportamiento muy parecido al de `01_baseline`, sin una mejora visible.

En conjunto, esta corrida indicó que aumentar el `batch_size` a 256 no fue una mejora efectiva para este problema. El cambio no rompió el entrenamiento, pero volvió el aprendizaje más lento y no produjo una política mejor que la obtenida en `03_stabilization_sde_off`.

Se puede ver el detalle de los resultados en la notebook eval y en el video.
