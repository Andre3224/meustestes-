import playsound
def calcmed(x,y):
    med = (x + y)/2
    return med

x = int(input('Digite uma nota: '))
y = int(input('Digite uma nota: '))
resultado = calcmed(x,y)

print(resultado)

if resultado < 6:
    playsound.playsound('seu-madruga-reprovado.mp3')
    print('REPROVADO')
    playsound.playsound('som-se-fodeu-gta-v.mp3')
    print('Bora recuperação!!!!!!!!!!!!!')
else:
    playsound.playsound('hoje-sim-hoje-nao.mp3')
    print('APROVADOOOO!!!!')
    playsound.playsound('vinheta-galvao-do-tetra.mp3')