import numpy as np
import os

# Funkcja generująca punkty na płaskiej poziomej powierzchni (XY, Z = const)
def generate_horizontal_plane(x_range, y_range, z_value, num_points):
    x = np.random.uniform(x_range[0], x_range[1], num_points)
    y = np.random.uniform(y_range[0], y_range[1], num_points)
    z = np.full(num_points, z_value)
    return np.column_stack((x, y, z))

# Funkcja generująca punkty na płaskiej pionowej powierzchni (XZ, Y = const)
def generate_vertical_plane(x_range, z_range, y_value, num_points):
    x = np.random.uniform(x_range[0], x_range[1], num_points)
    z = np.random.uniform(z_range[0], z_range[1], num_points)
    y = np.full(num_points, y_value)
    return np.column_stack((x, y, z))

# Funkcja generująca punkty na powierzchni cylindra
def generate_cylinder(radius, height_range, num_points):
    theta = np.random.uniform(0, 2*np.pi, num_points)
    z = np.random.uniform(height_range[0], height_range[1], num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return np.column_stack((x, y, z))

# Funkcja zapisująca dane do pliku .xyz
def save_to_xyz(points, filename):
    np.savetxt(filename, points, fmt="%.6f %.6f %.6f")

# Główna część programu
if __name__ == "__main__":
    output_dir = "generated_point_clouds"
    os.makedirs(output_dir, exist_ok=True)

    # Parametry
    num_points = 100000

    # Generowanie chmur punktów
    horizontal_plane = generate_horizontal_plane(x_range=(0, 10), y_range=(0, 10), z_value=0, num_points=num_points)
    vertical_plane = generate_vertical_plane(x_range=(0, 10), z_range=(0, 10), y_value=0, num_points=num_points)
    cylinder = generate_cylinder(radius=5, height_range=(0, 10), num_points=num_points)

    # Zapisywanie do plików
    save_to_xyz(horizontal_plane, os.path.join(output_dir, "horizontal_plane.xyz"))
    save_to_xyz(vertical_plane, os.path.join(output_dir, "vertical_plane.xyz"))
    save_to_xyz(cylinder, os.path.join(output_dir, "cylinder.xyz"))

    print(f"Pliki zapisane w folderze: {output_dir}")
