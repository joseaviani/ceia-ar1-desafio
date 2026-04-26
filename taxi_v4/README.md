# Aprendizaje por Refuerzo — Q-Learning Taxi-v4

**CEIA · Cohorte 21Co2025**

| Autor | Contacto |
|---|---|
| Ricardo Silvera | rsilvera@thalu.com.ar |
| José Aviani | jose.aviani@gmail.com |
| José Luis Diaz | diazjoseluis@gmail.com |

---

## Requisitos previos

- [pyenv](https://github.com/pyenv/pyenv#installation) — para manejar versiones de Python
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) — para aislar dependencias

## Setup

```bash
# Seleccionar Python 3.12
pyenv shell 3.12

# Crear y activar el entorno virtual
virtualenv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecutar la comparativa

```bash
python comparar.py
```

Al finalizar se genera el archivo `comparativa_epsilon.png` con las curvas de convergencia.

## Configurar qué estrategias comparar

Editá la lista `ESTRATEGIAS` al inicio de `comparar.py`:

```python
ESTRATEGIAS = [
    ['fijo', 0.2],       # epsilon fijo en 0.2
    ['dinamico', 0.9],   # epsilon que decae desde 0.9 hasta 0.01
    ['dinamico', 1.0],   # epsilon que decae desde 1.0 hasta 0.01
]
```

Cada entrada es `['fijo' | 'dinamico', epsilon_inicial]`. También podés ajustar `EPISODIOS` y `WINDOW` (ventana de la media móvil) en las líneas siguientes.

## Informe

Los resultados y conclusiones del experimento están documentados en [informe.pdf](informe.pdf).
