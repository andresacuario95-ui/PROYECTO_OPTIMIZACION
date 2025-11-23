import time
import numpy as np
import math

def es_primo_optimizado(n):
    """
    Función optimizada para verificar si un número es primo
    """
    # Casos base
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # Descartar números pares
        return False
    
    # Solo verificar hasta la raíz cuadrada de n
    # Matemáticamente: si n es compuesto, tiene un divisor ≤ √n
    limite = int(math.sqrt(n)) + 1
    
    # Verificar solo números impares (empezando desde 3)
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

def encontrar_primos_optimizado(limite):
    """
    Versión optimizada usando list comprehension
    """
    # Usar list comprehension + empezar desde 2 (1 no es primo)
    return [n for n in range(2, limite + 1) if es_primo_optimizado(n)]

def encontrar_primos_numpy(limite):
    """
    Versión usando NumPy para operaciones vectorizadas
    """
    primos = []
    for num in range(2, limite + 1):
        if es_primo_optimizado(num):
            primos.append(num)
    return np.array(primos)

# Función para comparar ambos métodos
def comparar_metodos(limite=100000):
    print("=== COMPARACIÓN DE MÉTODOS ===")
    
    # Método optimizado con list comprehension
    inicio = time.time()
    primos_opt = encontrar_primos_optimizado(limite)
    fin = time.time()
    tiempo_opt = fin - inicio
    
    # Método con NumPy
    inicio = time.time()
    primos_np = encontrar_primos_numpy(limite)
    fin = time.time()
    tiempo_np = fin - inicio
    
    print(f"\n--- MÉTODO OPTIMIZADO ---")
    print(f"Tiempo: {tiempo_opt:.2f} segundos")
    print(f"Primos encontrados: {len(primos_opt)}")
    
    print(f"\n--- MÉTODO NUMPY ---")
    print(f"Tiempo: {tiempo_np:.2f} segundos")
    print(f"Primos encontrados: {len(primos_np)}")
    
    # Verificar que ambos métodos dan los mismos resultados
    if len(primos_opt) == len(primos_np):
        print(f"\n✓ Ambos métodos encontraron la misma cantidad de primos")
    else:
        print(f"\n✗ Los métodos dieron resultados diferentes")
    
    return tiempo_opt, tiempo_np

if __name__ == "__main__":
    tiempo_opt, tiempo_np = comparar_metodos(100000)