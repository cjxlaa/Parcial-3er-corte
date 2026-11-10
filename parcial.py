import random

def bubble_sort(arr):
    n = len(arr)
    iteraciones = 0
    lista = arr.copy()
    
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            iteraciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
            
    return lista, iteraciones

def insertion_sort(arr):
    iteraciones = 0
    lista = arr.copy()
    
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        
        while j >= 0:
            iteraciones += 1
            if key < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = key
        
    return lista, iteraciones

def main():
    # Crear la lista aleatoria de 10 elementos únicos (1 al 100)
    lista_original = random.sample(range(1, 101), 10)
    
    while True:
        print("\n=== MENÚ DE ORDENAMIENTO ===")
        print(f"Lista original actual: {lista_original}")
        print("1. Ordenar mediante Bubble Sort (Burbuja)")
        print("2. Ordenar mediante Insertion Sort (Inserción)")
        print("3. Comparar iteraciones de ambos métodos")
        print("4. Generar una nueva lista aleatoria")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            lista_ord, iters = bubble_sort(lista_original)
            print(f"\n[Bubble Sort]")
            print(f"Lista ordenada: {lista_ord}")
            print(f"Total de iteraciones: {iters}")

        elif opcion == '2':
            lista_ord, iters = insertion_sort(lista_original)
            print(f"\n[Insertion Sort]")
            print(f"Lista ordenada: {lista_ord}")
            print(f"Total de iteraciones: {iters}")

        elif opcion == '3':
            _, iters_b = bubble_sort(lista_original)
            _, iters_i = insertion_sort(lista_original)
            
            print(f"\n--- COMPARACIÓN DE EFICIENCIA ---")
            print(f"• Bubble Sort:    {iters_b} iteraciones")
            print(f"• Insertion Sort: {iters_i} iteraciones")
            
            if iters_b < iters_i:
                print("-> Bubble Sort realizó menos iteraciones.")
            elif iters_i < iters_b:
                print("-> Insertion Sort realizó menos iteraciones.")
            else:
                print("-> Ambos algoritmos realizaron la misma cantidad de iteraciones.")

        elif opcion == '4':
            lista_original = random.sample(range(1, 101), 10)
            print(f"\nNueva lista generada con éxito: {lista_original}")

        elif opcion == '5':
            print("Ejecución finalizada.")
            break
        else:
            print("Opción no válida. Ingresa un número del 1 al 5.")

if __name__ == "__main__":
    main()