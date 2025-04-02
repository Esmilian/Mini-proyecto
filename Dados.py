#Dados de monopoly
import random
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

    #Simular Lanzar Dados
dado1, dado2 = lanzar_dados()
print(f"Haz lanzado los dados: {dado1} y {dado2}")
print(f"El total de los dados es: {dado1 + dado2}")
#Simular Lanzar Dados