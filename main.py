import sympy
x, y = sympy.symbols('x y')

#Value for X, to calculate the Y value in function of X
in_x = 5

#Insert the coordinates in the second and third row in the first and second element of each
A = sympy.Matrix([[x, y, 1], [-1, 3, 1], [2, 7, 1]])

det_A = A.det()
print("Determinant: ", det_A)

y_expr = sympy.solve(det_A, y)[0]
print("y =", y_expr)

subs_y_expr = y_expr.subs(x, in_x)
print(f"f({subs_y_expr}) =", subs_y_expr)


