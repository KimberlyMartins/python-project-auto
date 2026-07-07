#                     PYAUTOGUI
# O PyAutoGUI é uma biblioteca da linguagem Python que automatiza tarefas no computador. Ela funciona como um "robô", assumindo o controle do mouse e do teclado para clicar, mover, rolar e digitar, permitindo que você execute processos repetitivos exatamente como um humano faria.

#                       TIME 
#  A biblioteca time do Python é um módulo nativo usado para lidar com o tempo, medir a performance do código e pausar a execução do programa.

# No python usamos aspas sejam simples ou duplas para digitar palavras

#                   PASSO  A PASSO 
# 1- Entrar no sistema da empresa 
#     AUTOMATIZAR A ENTRADA NO WINDOWS PARA ABRIR O NAVEGADOR
# import pyautogui #Importamos a biblioteca pyautogui
# import time

# pyautogui.PAUSE = 1  #Seleciona o tempo de pausa para realizar as tarefas
# link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# pyautogui.press("win")
# pyautogui.write("chrome")
# pyautogui.press("enter")

# pyautogui.write(link)
# pyautogui.press("enter")
# time.sleep(3) 

# 2- LOGIN 


# 3- Abrir base de dados 


# 4- Cadastrar um produto


# 5- Repetir passo 4 até o fim da lista de produtos

# pip install pyautogui 

# pyautogui.click   = Clica
# pyautogui.write   = Escreve um texto
# pyautogui.press   = Aperta uma tecla
# pyautogui.hotkey  = Aperta um atalho (Hotkey)

import pyautogui #Importamos a biblioteca pyautogui
import time

pyautogui.PAUSE = 1  #Seleciona o tempo de pausa para realizar as tarefas
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Criamos a variável link

pyautogui.press("win") # Clica automaticamente na tecla windows
pyautogui.write("chrome") # Na aba windows digita chrome
pyautogui.press("enter") # Dá o enter no navegador chrome

pyautogui.write(link) # Escrevemos de forma automatica a variável criada no link
pyautogui.press("enter") # Pressionamos para a busca do link no navegador
time.sleep(3)  # Chamamos o time.sleep para fazer uma pausa maior evitando sobrecarga no site