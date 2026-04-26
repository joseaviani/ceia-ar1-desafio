## 08_validation_multiseed_seed1

### Configuración:

Dado que `07_longrun_bestcfg` había pasado a ser la mejor corrida obtenida hasta ese momento, para esta nueva prueba tomamos esa configuración como base y aplicamos un único cambio en el entrenamiento: modificar la **seed** de **0** a **1**. El objetivo no fue mejorar la política mediante un ajuste de hiperparámetros, sino comenzar una etapa de **validación multiseed** para analizar si el buen resultado de la corrida 07 era realmente robusto o si dependía de una seed particularmente favorable. En evaluación también aumentamos la cantidad de episodios evaluados a **20**, con el fin de obtener una estimación más representativa del comportamiento del agente.

## Resultados:

Los resultados cuantitativos mostraron un comportamiento muy inestable. En una primera etapa la corrida parecía prometedora: el `reward_mean` alcanzó aproximadamente **490.2** en 125k timesteps, **676.5** en 150k y **571.7** en 200k, lo que sugería que el agente estaba aprendiendo una política de buena calidad. Sin embargo, a partir de 300k se produjo un deterioro muy fuerte: el `reward_mean` cayó a aproximadamente **-31.9** en 300k, se mantuvo durante largos tramos cerca de cero o en valores negativos, y finalizó en apenas **-9.9** a 1.000.000 de timesteps.

En términos cualitativos, el video tampoco fue bueno: el auto lograba tomar algunas curvas, se salía de la pista, conseguía volver, pero luego continuaba **en sentido contrario**, lo que mostraba un comportamiento claramente incorrecto aunque todavía pudiera obtener cierta recompensa en algunos episodios.

En conjunto, esta corrida mostró que la configuración de `07_longrun_bestcfg` no era robusta frente a cambios de seed. Aunque durante una parte del entrenamiento aparecieron resultados cuantitativos altos, la política terminó colapsando y el análisis visual reveló un problema importante: una recompensa relativamente buena no garantizaba una conducción correcta. Esta corrida mostró que el reward por sí solo no alcanzaba para validar el comportamiento del agente y que era necesario complementar la evaluación con inspección visual.

Se puede ver el detalle de los resultados en la notebook eval y en el video.
