import pyautogui #Importação biblioteca de comandos.
import time #Importação de biblioteca de tempo.

pyautogui.hotkey('alt','tab') #Comando para executar o atalho "ALT"+"TAB"
time.sleep(0.3) #Comando para aguadar 3 milisegundos.
pyautogui.hotkey('alt','f4') #Comando para executar o atalho "ALT"+"F4"
pyautogui.press('alt') #Comando para executar a tecla "ALT"
pyautogui.press('right') #Comando para executar a tecla "Seta Direita"
pyautogui.press('enter') #Comando para executar a tecla "Enter"
pyautogui.press('down',5) #Comando para executar a tecla "Seta Baixo" 5 vezes
pyautogui.press('enter') #Comando para executar a tecla "Enter"