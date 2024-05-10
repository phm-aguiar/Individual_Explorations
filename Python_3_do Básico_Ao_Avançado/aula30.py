# "constantes"


velocidade = 61
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

multa_vel = (velocidade > RADAR_1)
multa_espaco = (local_carro >= (LOCAL_1 - RADAR_RANGE)
                ) and (local_carro <= (LOCAL_1 - RADAR_RANGE))
if multa_vel and multa_espaco:
    print("voce foi  multado")
else:
    print("voce nao foi multado")

