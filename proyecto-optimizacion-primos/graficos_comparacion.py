import matplotlib.pyplot as plt
import time
import codigo_original
import codigo_optimizado
import numpy as np

def generar_datos_comparativos():
    """Genera datos para comparar rendimiento en diferentes límites"""
    limites = [1000, 5000, 10000, 20000, 50000]
    tiempos_original = []
    tiempos_optimizado = []
    
    print("Generando datos comparativos...")
    
    for i, lim in enumerate(limites):
        print(f"Procesando límite {lim} ({i+1}/{len(limites)})")
        
        # Medir tiempo original
        inicio = time.time()
        codigo_original.encontrar_primos(lim)
        fin = time.time()
        tiempos_original.append(fin - inicio)
        
        # Medir tiempo optimizado
        inicio = time.time()
        codigo_optimizado.encontrar_primos_optimizado(lim)
        fin = time.time()
        tiempos_optimizado.append(fin - inicio)
    
    return limites, tiempos_original, tiempos_optimizado

def crear_graficos(limites, tiempos_original, tiempos_optimizado):
    """Crea gráficos comparativos"""
    
    # Gráfico 1: Comparación lineal
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(limites, tiempos_original, 'ro-', label='Código Original', linewidth=2, markersize=8)
    plt.plot(limites, tiempos_optimizado, 'go-', label='Código Optimizado', linewidth=2, markersize=8)
    plt.xlabel('Límite de búsqueda')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Tiempos de Ejecución')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfico 2: Mejora porcentual
    plt.subplot(1, 2, 2)
    mejora_porcentual = []
    for i in range(len(limites)):
        mejora = ((tiempos_original[i] - tiempos_optimizado[i]) / tiempos_original[i]) * 100
        mejora_porcentual.append(mejora)
    
    plt.bar(limites, mejora_porcentual, color='skyblue', alpha=0.7)
    plt.xlabel('Límite de búsqueda')
    plt.ylabel('Mejora (%)')
    plt.title('Mejora Porcentual del Código Optimizado')
    plt.grid(True, alpha=0.3)
    
    # Añadir valores en las barras
    for i, v in enumerate(mejora_porcentual):
        plt.text(limites[i], v + 1, f'{v:.1f}%', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('comparacion_rendimiento.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return mejora_porcentual

if __name__ == "__main__":
    # Generar datos
    limites, tiempos_original, tiempos_optimizado = generar_datos_comparativos()
    
    # Mostrar resultados en tabla
    print("\n" + "="*50)
    print("RESUMEN DE RESULTADOS")
    print("="*50)
    print(f"{'Límite':<10} {'Original (s)':<12} {'Optimizado (s)':<14} {'Mejora (%)':<12}")
    print("-"*50)
    
    for i in range(len(limites)):
        mejora = ((tiempos_original[i] - tiempos_optimizado[i]) / tiempos_original[i]) * 100
        print(f"{limites[i]:<10} {tiempos_original[i]:<12.2f} {tiempos_optimizado[i]:<14.2f} {mejora:<12.1f}")
    
    # Crear gráficos
    mejora_porcentual = crear_graficos(limites, tiempos_original, tiempos_optimizado)
    
    print(f"\nMejora promedio: {np.mean(mejora_porcentual):.1f}%")