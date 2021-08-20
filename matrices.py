import numpy as np
import os

def pausa():
    print("<Enter> para continuar...")
    input()
    os.system("clear")

os.system("clear")

print("OPERACIONES CON MATRICES ==>")

# Arreglos que simulan matrices ----------------------------
a = np.array([[1,2], [3,4]])

print("ARREGLOS COMO MATRICES")
print(f"a=\n{a}")
print(f"a + a=\n{a + a}")

pausa()

# Matrices de verdad ---------------------------------------
m = np.matrix([[5,7],[8,9]])

print("MATRICES DE VERDAD")
print(f"m=\n{m}")
print(f"m + m=\n{m + m}")

pausa()

# Sumando arreglos y matrices ------------------------------

print("SUMANDO ARREGLOS Y MATRICES")
print(f"a=\n{a}")
print(f"m=\n{m}")

print(f"a + m=\n{a + m}")
pausa()

# Producto de un escalar por una matriz -------------------

print("MULTIPLICANDO UNA MATRIZ POR UN ESCALAR")
print(f"a=\n{a}")
print(f"2 * a=\n{2 * a}")
pausa()

# Multiplicando matrices --------------------------------

print("MULTIPLICACION DE MATRICES (ALGEBRA LINEAL)")
print(f"a=\n{a}")
print(f"m=\n{m}")

print(f"a @ m=\n{a @ m}")
pausa()

# Matriz transpuesta -----------------------------------

print("MATRIZ TRANSPUESTA")
print(f"m=\n{m}")
print(f"m.T=\n{m.T}")

pausa()

# Determinante de una matriz ---------------------------
determinante = np.linalg.det(a)

print("DETERMINANTE DE UNA MATRIZ")
print(f"a=\n{a}")
print(f"|A|={determinante}")
pausa()

# Inversa de una matriz --------------------------------
inversa = np.linalg.inv(a)

print("INVERSA DE UNA MATRIZ Y SU COMPROBACION CON LA MATRIZ IDENTIDAD")
print(f"a=\n{a}")
print(f"A-1=\n{inversa}")

identidad = a @ inversa

print(f"A * A-1 = \n{identidad}")
