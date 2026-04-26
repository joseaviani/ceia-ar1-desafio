## 11_resize_multiseed_seed1

### Configuración:

Dado que `10_observation_resize` había pasado a ser la mejor corrida obtenida hasta ese momento, para esta nueva prueba decidimos comenzar la validación multiseed de esa nueva configuración. Tomamos como base `10_observation_resize` y aplicamos un único cambio en el entrenamiento: modificar la **seed** de **0** a **1**. El objetivo no fue introducir una mejora adicional mediante tuning, sino verificar si la mejora observada con el resize a `(84, 84)` era realmente robusta o si seguía dependiendo de una seed particularmente favorable, como había ocurrido con las corridas basadas en `07_longrun_bestcfg`.

## Resultados:

Los resultados cuantitativos fueron nuevamente muy buenos. Aunque la corrida comenzó con rewards bajos o negativos durante las primeras evaluaciones, a partir de aproximadamente 175k timesteps el agente mostró una mejora clara y sostenida: alcanzó alrededor de **334.6** en 175k, **597.3** en 350k, **753.7** en 375k, **833.3** en 400k, **577.7** en 875k, **632.8** en 925k, **744.0** en 975k y finalizó en **785.1** a 1.000.000 de timesteps. Estos valores fueron del mismo orden que los de `10_observation_resize`, lo que ya constituía una señal positiva respecto de la robustez de la nueva representación visual.

En términos cualitativos, el video mostró un comportamiento muy similar al de la corrida 10, con una conducción claramente más estable y consistente que la observada en las familias anteriores.

En conjunto, esta corrida fue una evidencia importante a favor del cambio de observación introducido en `10_observation_resize`. A diferencia de lo que había ocurrido con la validación multiseed de `07_longrun_bestcfg`, aquí la seed 1 no produjo un colapso del entrenamiento ni un comportamiento visual incorrecto. Por el contrario, los resultados mostraron que el resize a `(84, 84)` no solo mejoraba una corrida aislada, sino que también aumentaba la robustez de la configuración frente al cambio de seed. Esto reforzó la idea de que una parte importante del problema estaba en la representación visual original.

Se puede ver el detalle de los resultados en la notebook eval y en el video.
