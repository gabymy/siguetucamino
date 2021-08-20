import random
import time

def mostrarIntroduccion():
    print('Acabas de despertar, en una tierra desconocida. No salis de tu asombro') 
    time.sleep(2)
    print('ya que te habias dormido placidamente en tu cama.')
    time.sleep(2)
    print('Miras alrededor y descubres, dos cuevas:')
    time.sleep(2)
    print('ignoras que hay dentro, pero tenes que escoger una sola')
    time.sleep(2)
    print('Con la poca luz que hay, distinguis que una cueva esta llena de brillo en su interior')
    time.sleep(2)
    print('La otra, enama luces de colores pero es mas brillante')
    time.sleep(2)
    print('En las dos hay ruidos que parecen rugidos...')
    time.sleep(2)
    
def elegirCueva():
        cueva = ''
        while cueva != '1' and cueva != '2':
         print('¿a que cuevas queres entrar (1 o 2)')
         cueva = input()
        
        return cueva
    
def explorarCueva(cuevaElegida):
    print('Lleno de temor, te estas acercando a la cueva...')
    time.sleep(2)
    print('Descubres que lo que veias era solo una ilusion: Ninguna tiene luces...')
    time.sleep(2)
    print('Huele como a azufre y esta muy humedo...')
    time.sleep(2)
    print('Subitamente y para tu horrror ¡Un enorme dragon aparece delante tuyo! abre grande sus fauces')
    print('Te envuelve una rafaga de aliento pestido')
    time.sleep(2)
    print('¡No hay escapatoria posible!')
    print()
    time.sleep(2)
    
    cuevaAmigable = random.randint (1, 2)
    
    if cuevaElegida == str(cuevaAmigable):
        print('y......¡Te despertas en tu cama!')
    else:
        print('y.....¡Te come de un solo bocado!')
        
jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':
    
    mostrarIntroduccion()
    
    numeroDeCueva = elegirCueva()
    
    explorarCueva(numeroDeCueva)
    
    print('¿Queres jugar de nuevo? (si o no)')
    jugarDeNuevo = input()            
            
        