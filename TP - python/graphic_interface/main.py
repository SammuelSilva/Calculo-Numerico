import metodos

#integral = metodos.calculoTrapezio("1/x", 4, 2.0, 8.0)
#integral = metodos.calculoPrimeiraSimpson("1/(1+(x**2))",4,0.0,1.0)
integral = metodos.calculoSegundaSimpson("1/x",15,5.0,2.0)
print("integral")
print(integral)
