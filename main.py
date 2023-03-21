import sympy
x, y = sympy.symbols('x y')

#Encontrar a equação da reta com as coordenadas dela

#INPUT
#Value for X, to calculate the Y value in function of X
in_x = 5

#INPUT
#Insert the coordinates in the second and third row in the first and second element of each
point1 = (-1, 3)
point2 = (2, 7)

#calculation
A = sympy.Matrix([[x, y, 1], [point1[0], point1[1], 1], [point2[0], point2[1], 1]])

det_A = A.det()
print("Determinant =", det_A)

y_expr = sympy.solve(det_A, y)[0]
print("y =", y_expr)

subs_y_expr = y_expr.subs(x, in_x)
print(f"f({subs_y_expr}) =", subs_y_expr)


