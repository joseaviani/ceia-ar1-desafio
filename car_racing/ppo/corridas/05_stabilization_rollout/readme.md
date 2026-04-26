## 05_stabilization_rollout

### Configuración:

Dado que `03_stabilization_sde_off` seguía siendo la mejor corrida hasta ese momento, para esta nueva prueba tomamos esa configuración como base y aplicamos un único cambio: aumentar `n_steps` de **512** a **1024**. El motivo fue que, dado que el agente mostraba una política que aprendía parcialmente pero seguía siendo inestable, podía tener sentido probar rollouts más largos para que PPO construyera actualizaciones con más contexto temporal. Mantuvimos todo lo demás igual para poder evaluar de manera aislada el efecto de este cambio.

## Resultados:

Los resultados cuantitativos fueron claramente peores que los de `03_stabilization_sde_off`. El `reward_mean` se mantuvo negativo o muy bajo durante casi toda la corrida: comenzó alrededor de **-58.2** en 25k timesteps, siguió en valores similares hasta 125k, recién mostró una leve mejora en 150k con aproximadamente **1.3**, volvió a caer en 175k y terminó en apenas **96.8** a 200k. En comparación con `03_stabilization_sde_off`, esta corrida nunca logró una fase de aprendizaje fuerte y sostenida.

En términos cualitativos, el video también fue claramente malo: el auto se salía de la pista en la primera curva y no lograba recuperarse, por lo que el comportamiento observado fue directamente peor que el de las mejores corridas previas.

En conjunto, esta corrida mostró que aumentar `n_steps` a 1024 no fue una mejora para este problema: utilizar rollouts más largos no ayudaba a resolver el problema de estabilidad que observábamos.

Se puede ver el detalle de los resultados en la notebook eval y en el video.
