import pyautogui
import time

#criar um alerta para iniciação do programa
pyautogui.alert("O código vai começar, não mexa em nada!! ")
pyautogui.PAUSE = 1
#Primeiro passo precionar o botao windows 
pyautogui.press('winleft')
#Segundo passo escrever firefox 
pyautogui.write('firefox')
#terceiro passo precionar enter abrir firefox
pyautogui.press('enter')
time.sleep(5)
#quarto passo escrever youtube 
pyautogui.write('https://www.youtube.com/')
time.sleep(3)
#quinto passo precionar enter 
pyautogui.press('enter')
time.sleep(10)
#clicar com mouse em cima da pesquisa 
pyautogui.click(396,119)
time.sleep(3)
#sexto passo digitar louvor
pyautogui.write('Louvor')
time.sleep(2)
#setimo precionar enter 
pyautogui.press('enter')
time.sleep(2)
#oitavo com o mouse clicar em um louvor 
pyautogui.click(650,225)
time.sleep(15)
#nono clicar play
pyautogui.click(336,347)
time.sleep(2)
pyautogui.alert("O código acabou Curta o Louvor ")