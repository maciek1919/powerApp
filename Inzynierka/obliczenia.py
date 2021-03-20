

m1 = 50
m2 = 80
h1 = 180
J = 0.000193152  #moment bezwładnosci krazka podany w kg*m^2
r = 0.0685 #promien krazka w m
m_sum = 7.4484 + 0.76694*m2 - 0.05192 * h1 + m1  #dla masy ciala 80, ciezaru 50, wzrost 180 - 109,458kg
g = 9.8 # przyspieszenie ziemnskie w m/s^2
A = J + (m_sum * r**2)
B = m_sum * g * r
Fsmyczy = 150/1000 * g
C = Fsmyczy * r
t_s = 0.1 # czas probkowania w sek
rad = 3.14/200
fik_2 = 399 * rad
fik_1 = 308 * rad
fik = 235 * rad
fi_prim = (fik - fik_1)/t_s# pierwsza pochodna kąta
fi_bis = (fik - 2*fik_1 + fik_2)/(t_s**2)# druga pochodna kąta (2*fik_1 > fik+fik_2) - zdarzaja sie ujemne wartosci
P_lift = A*fi_prim*fi_bis + B*fi_prim + C*fi_prim # moc całkowita wyrażona w W
print( " ----MOC---- ", "{:.2f}".format(P_lift), " FI akt: ", fik, "FI pop: ", fik_1, "FI poppop: ", fik_2, " A: ", A, "B: ", B, "C: ", C , " pochodna1: ", fi_prim, " pochodna2: ", fi_bis )




