import cProfile
import pstats
import codigo_original
import codigo_optimizado

def profiling_original():
    """Profiling del código original"""
    print("=== PROFILING CÓDIGO ORIGINAL ===")
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Ejecutar con límite más pequeño para profiling rápido
    codigo_original.encontrar_primos(10000)
    
    profiler.disable()
    
    # Guardar resultados
    with open('profiling_original.txt', 'w') as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats('time')
        stats.print_stats()
    
    # Mostrar resumen en consola
    print("Top 10 funciones más lentas:")
    stats = pstats.Stats(profiler)
    stats.sort_stats('time')
    stats.print_stats(10)

def profiling_optimizado():
    """Profiling del código optimizado"""
    print("\n=== PROFILING CÓDIGO OPTIMIZADO ===")
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Ejecutar con mismo límite para comparación justa
    codigo_optimizado.encontrar_primos_optimizado(10000)
    
    profiler.disable()
    
    # Guardar resultados
    with open('profiling_optimizado.txt', 'w') as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats('time')
        stats.print_stats()
    
    # Mostrar resumen en consola
    print("Top 10 funciones más lentas:")
    stats = pstats.Stats(profiler)
    stats.sort_stats('time')
    stats.print_stats(10)

if __name__ == "__main__":
    profiling_original()
    profiling_optimizado()