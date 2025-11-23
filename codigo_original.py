import time

def es_primo(n):
    """
    Función original que verifica si un número es primo
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def encontrar_primos(limite):
    """
    Encuentra todos los números primos hasta el límite especificado
    """
    primos = []
    for num in range(1, limite + 1):
        if es_primo(num):
            primos.append(num)
    return primos

# Medición de tiempo de ejecución
if __name__ == "__main__":
    print("=== CÓDIGO ORIGINAL ===")
    inicio = time.time()
    
    # Buscar primos hasta 100,000
    primos = encontrar_primos(100000)
    
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.2f} segundos")
    print(f"Se encontraron {len(primos)} números primos")
    print(f"Últimos 5 primos encontrados: {primos[-5:]}")