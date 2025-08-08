class TransportSystem:
    def __init__(self):
        # Estaciones
        # Poner las estaciones que hacen falta 
        self.estaciones = [
            "San Isidro", "Belenes", "Tabachines", "Periférico Norte", 
            "Independencia Norte", "Zoquipan", "Plaza Patria", "División del Norte", 
            "Vallarta", "Colón", "Mezquitán", "Facultad de Medicina", 
            "Seminario", "Américas", "Juárez", "San Juan de Dios", 
            "Washington", "Agua Azul", "Parque Metropolitano", "Estampida", 
            "Monumento", "CUCEI", "Unidad Deportiva", "El Dean", 
            "Abastos", "Fray Angélico", "Periférico Sur", "Adolf Horn"
        ]
        
        # ID de las lineas
        # Agregar las lines faltantes
        self.station_lines = {
            0: {"line": "Línea 1", "color": "Amarillo"},
            1: {"line": "Línea 1", "color": "Amarillo"},
            2: {"line": "Línea 2", "color": "Naranja"},
            3: {"line": "Línea 3", "color": "Azul"},
            4: {"line": "Línea 1", "color": "Amarillo"},
            5: {"line": "Línea 2", "color": "Naranja"},
            6: {"line": "Línea 1", "color": "Amarillo"},
            7: {"line": "Línea 2", "color": "Naranja"},
            8: {"line": "Línea 1", "color": "Amarillo"},
            9: {"line": "Línea 3", "color": "Azul"},
            10: {"line": "Línea 1", "color": "Amarillo"},
            11: {"line": "Línea 2", "color": "Naranja"},
            12: {"line": "Línea 1", "color": "Amarillo"},
            13: {"line": "Línea 3", "color": "Azul"},
            14: {"line": "Centro", "color": "Verde"},
            15: {"line": "Centro", "color": "Verde"},
            16: {"line": "Línea 1", "color": "Amarillo"},
            17: {"line": "Línea 3", "color": "Azul"},
            18: {"line": "Línea 3", "color": "Azul"},
            19: {"line": "Línea 2", "color": "Naranja"},
            20: {"line": "Línea 1", "color": "Amarillo"},
            21: {"line": "Línea 3", "color": "Azul"},
            22: {"line": "Línea 2", "color": "Naranja"},
            23: {"line": "Línea 2", "color": "Naranja"},
            24: {"line": "Línea 2", "color": "Naranja"},
            25: {"line": "Línea 1", "color": "Amarillo"},
            26: {"line": "Línea 1", "color": "Amarillo"},
            27: {"line": "Línea 1", "color": "Amarillo"},
        }
        
        self.n = len(self.estaciones)
        self.INF = float('inf')
        
        # Matriz 
        self.matM = [
            [0, 1, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [1, 0, 2, 2, self.INF, self.INF, 7, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, 2, 0, 3, 2, self.INF, self.INF, 5, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [2, 2, 3, 0, 2, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, 2, 2, 0, 3, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, 3, 0, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, 7, self.INF, self.INF, self.INF, self.INF, 0, 4, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF],
            [self.INF, self.INF, 5, self.INF, self.INF, self.INF, 4, 0, 3, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, 3, 0, 2, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF],
            [self.INF, self.INF, self.INF, 3, self.INF, 3, self.INF, self.INF, 2, 0, self.INF, self.INF, self.INF, 4, 3, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, 0, 4, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, 4, 0, 2, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, 2, 0, 1, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4, self.INF, self.INF, 1, 0, 2, self.INF, self.INF, 4, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, 2, 0, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 3, self.INF, self.INF, self.INF, 0, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, 3, 0, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4, self.INF, self.INF, 3, 0, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 0, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, 0, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 0, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, 4, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 0, 3, self.INF, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, 0, 2, self.INF, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 0, 3, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, 0, self.INF, self.INF, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 0, 2, self.INF],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 2, 0, 3],
            [self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 4, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, self.INF, 3, 0]
        ]
        
        self.next_matrix = None
        self.iniciar = False
        
    #Empieza el nodo    
    def initialize_next_matrix(self):
        self.next_matrix = [[-1 for _ in range(self.n)] for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    self.next_matrix[i][j] = i
                elif self.matM[i][j] != self.INF:
                    self.next_matrix[i][j] = j
    
    #Floyd
    def floyd_warshall(self):
        if not self.iniciar:
            self.initialize_next_matrix()
        
        # Algoritmo Floyd
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if (self.matM[i][k] != self.INF and 
                        self.matM[k][j] != self.INF and
                        self.matM[i][k] + self.matM[k][j] < self.matM[i][j]):
                        
                        self.matM[i][j] = self.matM[i][k] + self.matM[k][j]
                        self.next_matrix[i][j] = self.next_matrix[i][k]
        
        self.iniciar = True
    
    def reconstruct_path(self, start, end):
        """Reconstruye el camino más corto entre dos estaciones"""
        if not self.iniciar:
            self.floyd_warshall()
        
        if self.next_matrix[start][end] == -1:
            return []  # No hay camino
        
        path = [start]
        current = start
        
        while current != end:
            current = self.next_matrix[current][end]
            if current == -1:
                return []  # Error en la reconstrucción
            path.append(current)
        
        return path
    
    def find_station_by_name(self, name):
        """Encuentra el índice de una estación por su nombre (case-insensitive)"""
        name_lower = name.lower().strip()
        for i, station in enumerate(self.estaciones):
            if station.lower() == name_lower:
                return i
        return -1
    
    def calculate_route(self, start_name, end_name):
        """Calcula la ruta completa entre dos estaciones"""
        start_id = self.find_station_by_name(start_name)
        end_id = self.find_station_by_name(end_name)
        
        if start_id == -1:
            return {"error": f"Estación '{start_name}' no encontrada"}
        if end_id == -1:
            return {"error": f"Estación '{end_name}' no encontrada"}
        if start_id == end_id:
            return {"error": "Las estaciones de origen y destino son las mismas"}
        
        path = self.reconstruct_path(start_id, end_id)
        
        if not path:
            return {"error": "No se encontró una ruta entre las estaciones"}
        
        # Construir información detallada de la ruta
        route_steps = []
        total_distance = 0
        transfers = 0
        current_line = ""
        
        for i, station_id in enumerate(path):
            station_name = self.estaciones[station_id]
            station_info = self.station_lines.get(station_id, {"line": "Desconocida", "color": "Gris"})
            
            step = {
                "station": station_name,
                "line": station_info["line"],
                "color": station_info["color"],
                "action": "inicio" if i == 0 else ("destino" if i == len(path) - 1 else "continuar")
            }
            
            if i > 0:
                # Calcular distancia del paso anterior
                prev_station = path[i-1]
                step_distance = self.matM[prev_station][station_id] - (self.matM[prev_station][prev_station] if i > 1 else 0)
                total_distance += step_distance
                
                # Detectar transferencias
                if station_info["line"] != current_line and current_line != "":
                    transfers += 1
                    step["action"] = "transferencia"
                
                current_line = station_info["line"]
            else:
                current_line = station_info["line"]
            
            route_steps.append(step)
        
        # Calcular distancia total correcta
        total_distance = self.matM[start_id][end_id]
        
        return {
            "success": True,
            "route": route_steps,
            "total_distance": total_distance,
            "transfers": transfers,
            "total_stations": len(path)
        }
    
    def display_route(self, route_info):
        """Muestra la ruta de forma formateada"""
        if "error" in route_info:
            print(f"Error: {route_info['error']}")
            return
        
        print("\n" + "-"*50)
        print("RUTA RECOMENDADA")
        print("-"*50)
        
        for i, step in enumerate(route_info["route"]):
            print(f"{i+1}. {step['station']}")
            print(f"   Línea: {step['line']} ({step['color']})")
            print(f"   Acción: {step['action'].upper()}")
            
            if i < len(route_info["route"]) - 1:
                print(" -> ")
                print("")
        
        print("\n" + "-"*50)
        print("RESUMEN DEL VIAJE")
        print("-"*50)
        print(f"Usted paso por: {route_info['total_stations']} estaciones.")
        print(f"Transferencias: {route_info['transfers']}")
        print("-"*50)
    
    def show_all_stations(self):
        """Muestra todas las estaciones disponibles"""
        print("\n" + "="*40)
        print("ESTACIONES DISPONIBLES")
        print("="*40)
        
        for i, station in enumerate(self.stations):
            line_info = self.station_lines.get(i, {"line": "Desconocida", "color": "Gris"})
            print(f"{i+1:2d}. {station} - {line_info['line']} ({line_info['color']})")
        
        print("="*40)
    
    def interactive_mode(self):
        """Modo interactivo para buscar rutas"""
        print("Sistema de Rutas de Transporte Público")
        print("Algoritmo Floyd-Warshall")
        print("="*40)
        
        while True:
            print("\nOPCIONES:")
            print("1. Buscar ruta")
            print("2. Ver todas las estaciones")
            print("3. Salir")
            
            choice = input("\nSelecciona una opción (1-3): ").strip()
            
            if choice == "1":
                start_station = input("\nIngresa la estación de ORIGEN: ").strip()
                end_station = input("Ingresa la estación de DESTINO: ").strip()
                
                if not start_station or not end_station:
                    print("Por favor ingresa ambas estaciones.")
                    continue
                
                print("\nCalculando ruta...")
                route_info = self.calculate_route(start_station, end_station)
                self.display_route(route_info)
                
            elif choice == "2":
                self.show_all_stations()
                
            elif choice == "3":
                print("Gracias por usar el sistema de transporte!")
                break
                
            else:
                print("Opción no válida. Por favor selecciona 1, 2 o 3.")


def main():
    """Función principal"""
    transport_system = TransportSystem()
    transport_system.interactive_mode()


if __name__ == "__main__":
    main()