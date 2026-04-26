## 06_stabilization_entropy

### Configuración:

Dado que `03_stabilization_sde_off` seguía siendo la mejor corrida hasta ese momento, para esta nueva prueba tomamos esa configuración como base y aplicamos un único cambio: aumentar `ent_coef` de **0.0** a **0.01**. El motivo fue que, si bien la corrida 03 había mostrado una mejora clara en reward, el comportamiento del agente seguía siendo frágil y oscilatorio, por lo que consideramos que una pequeña presión extra hacia la exploración podía ayudar a obtener políticas más robustas y menos rígidas.

## Resultados:

Los resultados cuantitativos mostraron que esta corrida logró aprender, pero de manera más lenta y sin superar a `03_stabilization_sde_off`. El `reward_mean` se mantuvo en valores negativos durante una parte importante del entrenamiento: comenzó alrededor de **-29.7** en 25k timesteps, cayó incluso hasta aproximadamente **-83.1** en 100k, y recién a partir de 125k empezó a mostrar una mejora sostenida. Hacia el final alcanzó aproximadamente **230.0** en 175k y terminó en **307.1** a 200k. Aunque estos resultados fueron claramente mejores que los de corridas fallidas como `02_stabilization_lr` y `05_stabilization_rollout`, quedaron por debajo de `03_stabilization_sde_off`, tanto en el pico alcanzado como en el nivel de reward final.

En términos cualitativos, el video mostró un comportamiento muy parecido al baseline, sin una mejora visual clara respecto de las corridas anteriores.

Esta corrida indicó que introducir un `ent_coef = 0.01` no fue una mala dirección, pero tampoco produjo una mejora real sobre la mejor configuración disponible hasta ese momento. El agente siguió siendo capaz de aprender una política útil, pero el progreso fue más lento y el comportamiento observado no mostró un salto cualitativo. Por lo tanto, esta variante quedó como una alternativa razonable, aunque inferior a `03_stabilization_sde_off`.

Se puede ver el detalle de los resultados en la notebook eval y en el video.
