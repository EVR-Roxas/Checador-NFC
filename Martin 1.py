stations = [
    "San Isidro", "Belenes", "Tabachines", "Periférico Norte", "Independencia Norte", "Zoquipan",
    "Plaza Patria", "División del Norte", "Vallarta", "Colón", "Mezquitán", "Facultad de Medicina", 
    "Seminario", "Américas", "Juárez", "San Juan de Dios", "Washington", "Agua Azul", "Parque Metropolitano", 
    "Estampida", "Monumento", "CUCEI", "Unidad Deportiva", "El Dean", "Abastos", "Fray Angélico", 
    "Periférico Sur", "Adolf Horn"
]

connections = {
    0: {1: ("Línea 1 (Amarillo)", "Dirección a Periférico Norte")},
    1: {2: ("Línea 2 (Naranja)", "Dirección a Tetlán")},
    2: {3: ("Línea 3 (Azul)", "Dirección a Periférico Sur")},
    3: {4: ("Línea 4 (Verde)", "Dirección a Juárez")},
    4: {5: ("Línea 5 (Roja)", "Dirección a Periférico Sur")},
    5: {6: ("Línea 6 (Morada)", "Dirección a Tetlán")},
    6: {7: ("Línea 7 (Cyan)", "Dirección a El Dean")},
    7: {8: ("Línea 8 (Magenta)", "Dirección a Estampida")},
    8: {9: ("Línea 9 (Menta)", "Dirección a Periférico Norte")},
    9: {10: ("Línea 10 (Café)", "Dirección a Zapopan Centro")},
}

INF = float('inf')
matM = [
    [0, 1, INF, 2, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [1, 0, 2, 2, INF, INF, 7, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 2, 0, 3, 2, INF, INF, 5, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [2, 2, 3, 0, 2, INF, INF, INF, INF, 3, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, 2, 2, 0, 3, INF, INF, 2, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, 3, 0, INF, INF, INF, 3, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 7, INF, INF, INF, INF, 0, 4, INF, INF, 3, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, 5, INF, INF, INF, 4, 0, 3, INF, INF, 2, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, 2, INF, INF, 3, 0, 2, INF, INF, 2, INF, INF, INF, INF, INF],
    [INF, INF, INF, 3, INF, 3, INF, INF, 2, 0, INF, INF, INF, 4, 3, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, 3, INF, INF, INF, 0, 4, INF, INF, INF, 2, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, 2, INF, INF, 4, 0, 2, INF, INF, 3, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, 2, INF, INF, 2, 0, 1, INF, INF, 2, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 4, INF, INF, 1, 0, 2, INF, INF, 4],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, INF, INF, INF, 2, 0, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 2, 3, INF, INF, INF, 0, 3, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 2, INF, INF, 3, 0, 3],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 4, INF, INF, 3, 0]
]

def floyd():
    n = len(matM)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matM[i][k] + matM[k][j] < matM[i][j]:
                    matM[i][j] = matM[i][k] + matM[k][j]

def reconstruct_path(u, v):
    if matM[u][v] == INF:
        return []
    path = [u]
    while u != v:
        u = matM[u][v]
        path.append(u)
    return path

def show_path(start, end):
    start_id = stations.index(start)
    end_id = stations.index(end)

    path = reconstruct_path(start_id, end_id)

    if not path:
        print("No hay camino disponible.")
    else:
        print(f"\nRuta recomendada desde {start} hasta {end}:")
        for i, node in enumerate(path):
            current_station = stations[node]
            print(f"Estación: {current_station}")
            if i < len(path) - 1:
                next_station = stations[path[i + 1]]
                print(f"  - Mantente en la línea o cámbiate a otra línea en {next_station}")

print("Estaciones disponibles:")
for i, station in enumerate(stations):
    print(f"{station}")

start_station = input("Ingresa el nombre de la estación de inicio: ").strip()
end_station = input("Ingresa el nombre de la estación de destino: ").strip()

if start_station not in stations or end_station not in stations:
    print("Estación no válida. Por favor ingresa un nombre de estación válido.")
else:
    floyd()
    show_path(start_station, end_station)
