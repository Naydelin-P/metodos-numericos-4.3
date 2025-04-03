#   Codigo que implementa el metodo del trapecio 
#   para aproximar la integral
#   
# Naydelin Palomo Martinez
import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos

    # Regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    return integral

# Función de ejemplo
def funcion(x):
    return 200 * x  # Cambiar esta función según el problema

# Parámetros de integración
a, b = 0.1, 0.3  # Intervalo

# Bucle para calcular y graficar para diferentes valores de n
for n in [6, 10, 20, 30]:
    # Aproximación de la integral
    resultado = simpson_rule(funcion, a, b, n)
    print(f"La aproximación de la integral con n={n} subintervalos es: {resultado}")

    # Gráfica de la función y la aproximación con la regla de Simpson
    x_vals = np.linspace(a, b, 100)
    y_vals = funcion(x_vals)

    plt.plot(x_vals, y_vals, label=r"$f(x) = kx$", color="blue")
    plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
    plt.scatter(np.linspace(a, b, n + 1), funcion(np.linspace(a, b, n + 1)), color="red", label="Puntos de interpolación")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title(f"Aproximación de la integral con la regla de Simpson (n={n})")
    plt.grid()

    # Guardar la figura
    plt.savefig(f"simpson_n{n}.png")
    plt.show()
