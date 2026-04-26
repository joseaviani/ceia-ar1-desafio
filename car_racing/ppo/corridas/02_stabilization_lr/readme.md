## 02_stabilization_lr

### Configuración:

A partir de análisis de la corrida anterior decidimos aplicar un único cambio para esta nueva corrida: reducir el learning rate de 1e-4 a 5e-5. En la corrida anterior el agente parecía encontrar una política parcialmente buena pero luego degradarse, por lo que pensamos que las actualizaciones podían estar siendo demasiado agresivas. Reducir el learning rate era una forma simple y controlada de intentar estabilizar el entrenamiento, manteniendo todo lo demás exactamente igual para poder atribuir con claridad cualquier mejora o empeoramiento a ese único cambio.

## Resultados:

Los resultados de esta corrida fueron claramente peores que los de la anterior.

En términos cuantitativos, el reward_mean se mantuvo casi siempre en valores muy bajos o directamente negativos durante toda la ejecución: comenzó en aproximadamente -75.6 a 25k timesteps, tuvo una mejora leve y aislada hasta alrededor de 50.1 en 75k, pero luego volvió a oscilar cerca de cero o en terreno negativo, finalizando en 20.97 a 200k. Además, los episodios evaluados tuvieron en casi todos los casos una ep_length_mean de 1000 pasos, lo que indica que el agente muchas veces llegaba al límite de pasos sin lograr una conducción efectiva.

En términos cualitativos, el video mostró un comportamiento muy pobre: el auto oscilaba desde el comienzo, se salía de la pista en la primera curva, y luego continuaba girando sobre sí mismo fuera de la pista sin capacidad de recuperación.

En conjunto, estos resultados mostraron que la hipótesis inicial no se confirmó: reducir el learning rate no estabilizó el entrenamiento, sino que deterioró fuertemente el aprendizaje. Esto sugiere que, para esta configuración y este entorno, bajar el learning rate a 5e-5 hizo que las actualizaciones fueran demasiado débiles como para sostener el progreso que sí habíamos observado con 1e-4, por lo que esta dirección de ajuste quedó descartada.

Se puede ver el detalle de los resultados en la notebook eval y en el video.