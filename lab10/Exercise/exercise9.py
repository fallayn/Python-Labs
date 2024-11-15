import networkx as nx

def build_optimal_routes(warehouses, clients, road_distances):
    optimal_routes = {}
    for warehouse in warehouses:
        optimal_routes[warehouse] = {}
        for client in clients:
            shortest_path = nx.dijkstra_path(road_distances, warehouse, client)
            optimal_routes[warehouse][client] = shortest_path
    return optimal_routes

def total_delivery_time(warehouses, clients, road_distances, average_speed):
    delivery_times = {}
    for warehouse in warehouses:
        total_time = 0
        for client in clients:
            shortest_path = nx.dijkstra_path_length(road_distances, warehouse, client)
            total_time += shortest_path / average_speed
        delivery_times[warehouse] = total_time
    return delivery_times

def furthest_clients(warehouses, clients, road_distances):
    furthest = {}
    for warehouse in warehouses:
        max_distance = 0
        furthest_client = None
        for client in clients:
            distance = nx.dijkstra_path_length(road_distances, warehouse, client)
            if distance > max_distance:
                max_distance = distance
                furthest_client = client
        furthest[warehouse] = furthest_client, max_distance
    return furthest

def print_summary(warehouses, optimal_routes, delivery_times, furthest_clients):
    print("Optimal Routes:")
    for warehouse, routes in optimal_routes.items():
        print(f"From Warehouse {warehouse}:")
        for client, route in routes.items():
            print(f"To Client {client}: {' -> '.join(route)}")

    print("\nTotal Delivery Time from Each Warehouse:")
    for warehouse, time in delivery_times.items():
        print(f"Warehouse {warehouse}: {time} hours")

    print("\nFurthest Clients from Each Warehouse:")
    for warehouse, (client, distance) in furthest_clients.items():
        print(f"From Warehouse {warehouse} to Client {client}: {distance} units")

# Пример данных о расположении складов, клиентов и расстояниях между ними
warehouses = ['Warehouse1', 'Warehouse2']
clients = ['Client1', 'Client2', 'Client3']
road_distances = nx.Graph()
road_distances.add_edge('Warehouse1', 'Client1', weight=10)
road_distances.add_edge('Warehouse1', 'Client2', weight=15)
road_distances.add_edge('Warehouse1', 'Client3', weight=20)
road_distances.add_edge('Warehouse2', 'Client1', weight=12)
road_distances.add_edge('Warehouse2', 'Client2', weight=18)
road_distances.add_edge('Warehouse2', 'Client3', weight=25)

average_speed = 50  # средняя скорость доставки в км/ч

# Вызываем функции для получения сводной информации
optimal_routes = build_optimal_routes(warehouses, clients, road_distances)
delivery_times = total_delivery_time(warehouses, clients, road_distances, average_speed)
furthest_clients_info = furthest_clients(warehouses, clients, road_distances)

def print_solution():
    print_summary(warehouses, optimal_routes, delivery_times, furthest_clients_info)
