## 09_validation_multiseed_seed2

### Configuración:

Dado que `08_validation_multiseed_seed1` había mostrado que la configuración de `07_longrun_bestcfg` no era robusta frente al cambio de seed, para esta nueva corrida continuamos con la validación multiseed tomando nuevamente como base `07_longrun_bestcfg` y aplicando un único cambio en el entrenamiento: modificar la **seed** de **0** a **2**. Al igual que en la corrida anterior, el objetivo no fue mejorar la política mediante un nuevo ajuste de hiperparámetros, sino seguir evaluando si el buen resultado de `07_longrun_bestcfg` podía repetirse en distintas inicializaciones. También mantuvimos la evaluación sobre **20 episodios**, de manera consistente con la estrategia de validación iniciada en la corrida 08.

## Resultados:

Los resultados cuantitativos de esta corrida volvieron a ser altos durante gran parte del entrenamiento. El `reward_mean` mostró una mejora sostenida desde etapas relativamente tempranas, alcanzando aproximadamente **545.9** en 175k timesteps, **650.0** en 325k, **670.4** en 525k, **762.3** en 775k, **910.6** en 900k y finalizando en **807.5** a 1.000.000 de timesteps. Desde lo numérico, esta corrida parecía confirmar el potencial de la configuración y resultaba comparable con `07_longrun_bestcfg`.

Sin embargo, el análisis cualitativo volvió a mostrar un problema importante: en el video el auto se salía rápidamente de la pista, lograba volver, pero lo hacía **en dirección contraria**, reproduciendo un patrón de comportamiento incorrecto similar al observado en la corrida 08.

En conjunto, esta corrida reforzó una conclusión importante: obtener rewards altos no garantizaba una conducción correcta. A diferencia de `08_validation_multiseed_seed1`, aquí no hubo un colapso cuantitativo marcado, pero el video mostró igualmente una política inadecuada desde el punto de vista cualitativo. Esto confirmó que la configuración de `07_longrun_bestcfg` seguía teniendo un problema de robustez y que el reward del entorno, por sí solo, no era una métrica suficiente para validar la calidad real del agente.

Se puede ver el detalle de los resultados en la notebook eval y en el video.
