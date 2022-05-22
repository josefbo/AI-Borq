varLapso = 15

varColorI ="#F7FF87"
varColorF ="#FFF"

varTono1 = .25
varTono2 = .5
varTono3 = .75
varTono4 = 1

def inicio():
etapaUno()

def finalizar():
print("Luces encendidad a todo color.")

def timer(minutos):
print("Inicio conteo de 15" + str(minutos))

print("finaliza conteo de 15")


def etapaUno():
print("Etapa uno iniciada")
timer(varLapso)
luces(varTono1, varColorI)
print("Etapa uno finalizada")
etapaDos()

def etapaDos():
print("Etapa uno iniciada")
timer(varLapso)
luces(varTono2, varColorI)
print("Etapa dos finalizada")
etapaTres()

def etapaTres():
print("Etapa uno iniciada")
timer(varLapso)
luces(varTono3, varColorF)
print("Etapa tres finalizada")
etapaCuatro()

def etapaCuatro():
print("Etapa cuatro iniciada")
timer(varLapso)
luces(varTono4, varColorF)
print("Etapa uno finalizada")
finalizar()