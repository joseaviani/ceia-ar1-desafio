# Aprendizaje por Refuerzo — Desafíos

**CEIA · Cohorte 21Co2025**

| Autor | Contacto |
|---|---|
| Ricardo Silvera | rsilvera@thalu.com.ar |
| José Aviani | jose.aviani@gmail.com |
| José Luis Diaz | diazjoseluis@gmail.com |

---

## Sub-proyectos

### [Taxi-v4](taxi_v4/) — Q-Learning tabular

Resolución del entorno clásico Taxi-v4 mediante Q-Learning off-policy. El agente opera en una grilla de 5×5 con 500 estados discretos: debe recoger un pasajero y transportarlo a su destino. Se implementó la ecuación de Q-Learning con máscara de estados terminales `(1 − terminated)` y política ε-greedy con decaimiento exponencial. El experimento central compara epsilon dinámico vs. fijo, concluyendo que arrancar con exploración alta (ε = 0.9 con decay) permite cubrir el espacio de estados completo en los primeros episodios y converge a una recompensa promedio óptima de +8.0 a +8.5, mientras que un epsilon fijo bajo queda atrapado en un régimen subóptimo al explotar una tabla Q vacía. Ver [informe](taxi_v4/informe.pdf).

### [LunarLander-v3](lunar_lander/) — SARSA vs Q-Learning con discretización

Comparativa entre SARSA (on-policy) y Q-Learning (off-policy) sobre el entorno LunarLander-v3, que presenta un espacio de observación continuo de 8 variables. Al ser algoritmos tabulares, se discretizó el espacio de estados con bins no uniformes `[3, 5, 3, 6, 4, 3]` resultando en 12.960 estados. Se aplicaron técnicas de mejora como inicialización optimista de la Q-table (Q = 5.0) y reward shaping basado en potencial para guiar al agente ante la escasez de recompensa. Con 200.000 episodios, Q-Learning alcanzó una media de −98.4 puntos (+72.7 sobre la política aleatoria) frente a −154.9 de SARSA, confirmando la ventaja off-policy en este entorno. El análisis concluye que el enfoque tabular tiene limitaciones estructurales para espacios continuos, y señala DQN como paso natural siguiente. Ver [informe](lunar_lander/informe.pdf).

### [Car Racing](car_racing/) — PPO con observaciones visuales

Aplicación de PPO (Proximal Policy Optimization) al entorno CarRacing-v2, donde el agente aprende a conducir directamente desde píxeles con un espacio de acciones continuo (giro, aceleración, freno). Al combinar percepción visual y control continuo, este entorno requiere aprender simultáneamente representación y política. Se utilizó Stable-Baselines3 con wrappers para preprocesamiento de frames. Los experimentos exploraron el efecto de distintas configuraciones sobre la estabilidad del entrenamiento y la generalización a pistas nuevas. Se identifica SAC como alternativa promisoria por su exploración basada en entropía máxima, aunque no se implementó por limitaciones de tiempo.

Entre los problemas que trabajamos incluimos **Car Racing** porque representa un problema de aprendizaje por refuerzo completo: el agente debe **aprender a conducir a partir de imágenes**, tomando acciones continuas para maximizar una recompensa acumulada.

El problema consiste en entrenar un agente de aprendizaje por refuerzo capaz de conducir en **CarRacing-v3** a partir de observaciones visuales, tomando acciones continuas para controlar dirección, aceleración y freno. Se trata de un problema exigente porque combina **percepción visual**, **control continuo**, **estabilidad temporal** y **generalización** a distintas pistas. La solución se abordó utilizando **Gymnasium** como framework del entorno y **PPO** como algoritmo base, implementado con **Stable-Baselines3**. A partir de una configuración inicial con imágenes en grayscale, frame stacking y política convolucional, se construyó un baseline y luego se fue iterando experimentalmente sobre distintas variantes, modificando de a un parámetro por vez para poder analizar con claridad el efecto de cada cambio.

Durante el trabajo aparecieron varios inconvenientes. En primer lugar, hubo dificultades técnicas de implementación y compatibilidad, especialmente en **Windows con VS Code**, relacionadas con serialización, vectorización de entornos, formatos de observación y consistencia entre entrenamiento y evaluación; estos problemas se resolvieron corrigiendo wrappers, ajustando el pipeline visual y asegurando que train y eval usaran exactamente el mismo espacio de observación. En segundo lugar, aparecieron problemas propios del entrenamiento: algunas configuraciones lograban rewards altos pero generaban comportamientos incorrectos, como salirse de pista o volver en sentido contrario. Esto mostró que el reward por sí solo no alcanzaba para validar la calidad de la política, por lo que fue necesario complementar la evaluación cuantitativa con análisis cualitativo mediante videos y métricas adicionales como *completion rate*. A nivel experimental, se probaron distintos ajustes de PPO; varios no mejoraron o incluso empeoraron el resultado, mientras que la mejor mejora surgió al **reducir el tamaño de la observación mediante resize a `(84,84)`**, lo que permitió obtener una política más estable y una conducción visualmente superior. En síntesis, el problema se resolvió mediante un proceso iterativo de experimentación controlada, donde cada dificultad fue guiando ajustes concretos tanto en la implementación como en la formulación de la observación y la evaluación.

Cada folder de la solución tiene el detalle de lo ejecutado, los cambios, la explicación de cada corrida, etc:

- [`Car Racing`](car_racing/readme.md)

- [`Car Racing/PPO`](car_racing/ppo/readme.md)