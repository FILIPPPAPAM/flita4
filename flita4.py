from generator import *
import time

def get_vertices_with_even_degree(adj_matrix):
    n = len(adj_matrix)
    degrees = [0] * n  # Список для хранения степеней вершин

    # Вычисление степеней вершин
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == '1':
                if i==j:
                    degrees[i] += 2
                else:
                    degrees[i] += 1

    even_degree_vertices = []  # Список для хранения вершин с четной степенью

    # Поиск вершин с четной степенью
    for i in range(n):
        if degrees[i] % 2 == 0:
            even_degree_vertices.append(i+1)

    return even_degree_vertices


def bubble_sort(vertices):
    n = len(vertices)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if vertices[j] < vertices[j + 1]:
                vertices[j], vertices[j + 1] = vertices[j + 1], vertices[j]



with open('qq.txt', 'w') as file1:
    for i in range(40000, 40004, 2000):
        create_mirror_matrix(i)
        a = r"matrix.txt"

        with open(a, 'r') as file:
            adj = [line.split() for line in file]
        vert = get_vertices_with_even_degree(adj)
        start_time = time.time()
        bubble_sort(vert)
        end_time = time.time()
        t = str(i)+' '+'{:.8f}'+'\n'
        file1.write(t.format(end_time-start_time))
        print(i)