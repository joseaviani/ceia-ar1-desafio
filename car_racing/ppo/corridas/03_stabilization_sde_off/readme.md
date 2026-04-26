## 03_stabilization_sde_off

### Configuración:

Dado que en `02_stabilization_lr` reducir el learning rate empeoró claramente el aprendizaje, para esta nueva corrida volvimos a la configuración de `01_baseline` y aplicamos un único cambio: desactivar `use_sde` (`use_sde = False`). El motivo fue que en `01_baseline` el agente mostraba oscilaciones visibles en rectas y curvas, por lo que consideramos que parte de esa inestabilidad podía estar asociada a un esquema de exploración demasiado ruidoso para este entorno. Mantuvimos todo lo demás igual.

## Resultados:

Los resultados cuantitativos de esta corrida fueron claramente mejores que los de `01_baseline` y muy superiores a los de `02_stabilization_lr`. El `reward_mean` comenzó en valores negativos durante las primeras evaluaciones, pero a partir de 75k timesteps mostró una mejora fuerte y sostenida: llegó a aproximadamente **190.1** en 75k, **318.1** en 100k, **350.5** en 150k, alcanzó un pico de **490.6** en 175k y finalizó en **326.2** a 200k.

Sin embargo, en el plano cualitativo el video no mostró una mejora equivalente: el auto tomaba correctamente la primera curva, pero comenzaba a oscilar en la segunda recta, se salía de la pista más temprano que en `01_baseline`, llegaba a la siguiente curva por fuera de la pista y luego seguía recto fuera de ella.

Esta corrida mostró por un lado que desactivar `use_sde` mejoró el rendimiento cuantitativo y permitió sostener una política con rewards altos durante buena parte del entrenamiento, pero por otro lado mostró que el comportamiento visual siguió siendo frágil y no resolvió el problema central de estabilidad, ya que el agente todavía perdía la pista relativamente pronto y no mostraba una recuperación robusta.

Se puede ver el detalle de los resultados en la notebook eval y en el video.
